import os
import sys
from gnome_keyring_gpg_unlock.interface.cli.abstract import BaseCommand
from gnome_keyring_gpg_unlock.GpgSecret import GpgSecret
import getpass

class Setup(BaseCommand):

  def run(self, secret: str, public_key: str) -> bool:
    self.setupSecret(secret, public_key)
    self.setupService(secret)

    return True

  def setupSecret(self, secret: str, public_key) -> bool:
    gpgSecret = GpgSecret()
    if os.path.isfile(secret):
      answer = self.interface.askFor('Secret already exists. Do you want to overwrite it?', ['y', 'n'], 'n')
      if answer != 'y':
        return False

    gpgSecret.encrypt(getpass.getpass(), public_key, secret)
    del gpgSecret # remove gpgSecret object from memory

    return True


  def setupService(self, secret: str) -> bool:
    HOME = os.environ.get('HOME')
    EXEC_PATH = sys.argv[0]
    SERVICE_PATH = f'{HOME}/.config/systemd/user/gnome-keyring-gpg-unlock.service'

    service = f"""
    [Unit]
    Description=This unlocks your default gnome-keyring at startup, using your gpg-encrypted password
    BindsTo=gnome-session.target
    [Service]
    Type=oneshot
    ExecStart={EXEC_PATH} unlock --secret {secret}

    [Install]
    WantedBy=gnome-session.target
    """

    with open(SERVICE_PATH, "w") as serviceFile:
        serviceFile.write(service)
        serviceFile.close()

    self.cli.execute('systemctl --user daemon-reload')
    self.cli.execute('systemctl --user enable gnome-keyring-gpg-unlock.service')

    return True
