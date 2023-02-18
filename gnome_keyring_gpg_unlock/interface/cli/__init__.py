import sys

import simpcli
from simpcli import CliException

from gitcd.interface.cli.clean import Clean

from gnome_keyring_gpg_unlock.interface.cli.abstract import BaseCommand
from gnome_keyring_gpg_unlock.interface.cli.setup import Setup
from gnome_keyring_gpg_unlock.interface.cli.unlock import Unlock


class Cli():

    interface = simpcli.Interface()

    commands = [
        'setup',
        'unlock'
    ]

    def getAvailableCommands(self):
        return self.commands

    def instantiateCommand(self, command: str) -> BaseCommand:
        if command == 'setup':
            return Setup()
        if command == 'unlock':
            return Unlock()
        # probably best to implement a default command
        # for command-not-found error

    def dispatch(self, command: str, secret: str, public_key: str):
        try:
            commandObject = self.instantiateCommand(command)
        except Exception as e:
            self.interface.error(
                e
            )
            sys.exit(1)

        self.interface.header('gnome-keyring-gpg-unlock %s' % (command))

        
        commandObject.run(secret, public_key)

    def close(self, msg: str):
        self.interface.ok(msg)
