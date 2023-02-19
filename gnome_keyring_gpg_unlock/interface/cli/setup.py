import os
from gnome_keyring_gpg_unlock.interface.cli.abstract import BaseCommand
from gnome_keyring_gpg_unlock.GpgSecret import GpgSecret
import getpass

class Setup(BaseCommand):

  def run(self, secret: str, public_key: str):
    gpgSecret = GpgSecret()

    gpgSecret.encrypt(getpass.getpass(), public_key, secret)
    del gpgSecret # remove gpgSecret object from memory

    HOME = os.environ.get('HOME')
    EXEC_PATH = f'{HOME}/.local/bin/gnome-keyring-gpg-unlock'
    SERVICE_PATH = f'{HOME}/.config/systemd/user/gnome-keyring-gpg-unlock.service'



    service = f"""
    [Unit]
    Description=This unlocks your default gnome-keyring at startup, using your gpg-encrypted password
    BindsTo=gnome-session.target
    [Service]
    Type=oneshot
    ExecStartPre=/bin/sleep 5 # give the ui time to build up a little, leads to strange behavior without this timeout
    ExecStart={EXEC_PATH} unlock --secret {secret}

    [Install]
    WantedBy=gnome-session.target
    """

    with open(SERVICE_PATH, "w") as serviceFile:
        serviceFile.write(service)
        serviceFile.close()

    self.cli.execute('systemctl --user daemon-reload')
    self.cli.execute('systemctl --user enable gnome-keyring-gpg-unlock.service')
