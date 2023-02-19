from gnome_keyring_gpg_unlock.interface.cli.abstract import BaseCommand
from gnome_keyring_gpg_unlock.GpgSecret import GpgSecret
import getpass

class Setup(BaseCommand):

    def run(self, secret: str, public_key: str):
        gpgSecret = GpgSecret()

        gpgSecret.encrypt(getpass.getpass(), public_key, secret)
        del gpgSecret # remove gpgSecret object from memory

        print('Run Setup, which means encrypting the password and setup autostart')
