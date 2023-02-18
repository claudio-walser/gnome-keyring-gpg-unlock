from gnome_keyring_gpg_unlock.interface.cli.abstract import BaseCommand


class Unlock(BaseCommand):

    def run(self, secret: str, public_key: str):
        print('Unlock the default keyring')