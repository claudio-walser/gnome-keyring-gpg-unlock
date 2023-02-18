from gnome_keyring_gpg_unlock.interface.cli.abstract import BaseCommand


class Setup(BaseCommand):

    def run(self, secret: str, public_key: str):
        print('Run Setup, which means encrypting the password and setup autostart')