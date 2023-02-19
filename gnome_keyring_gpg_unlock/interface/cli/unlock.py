from gnome_keyring_gpg_unlock.interface.cli.abstract import BaseCommand

from gnome_keyring_gpg_unlock.GpgSecret import GpgSecret
from gnome_keyring_gpg_unlock.Keyring import Keyring

class Unlock(BaseCommand):

    def run(self, secret: str, public_key: str = ''):
        gpgSecret = GpgSecret()
        keyringPassword = gpgSecret.decrypt(secret)
        keyring = Keyring()
        keyring.unlock(keyringPassword)

        del keyringPassword, gpgSecret, keyring # remove instances from memory
