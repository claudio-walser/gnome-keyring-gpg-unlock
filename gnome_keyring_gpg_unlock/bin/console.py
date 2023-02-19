#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import sys
import argcomplete
import argparse
from gnome_keyring_gpg_unlock.interface.cli import Cli

import sys

import os
from pprint import pprint

cli = Cli()

# create parser in order to autocomplete
parser = argparse.ArgumentParser()

parser.add_argument(
    "command",
    help="Command to call.",
    type=str,
    choices=cli.getAvailableCommands()
)
parser.add_argument(
    "--secret",
    help="Your secret file, storing your gpg encrypted password",
    type=str
)
parser.add_argument(
    "--public-key",
    help="Your gpg public key to encrypt the password with",
    type=str
)
argcomplete.autocomplete(parser)


def main():


    file_path = os.path.realpath(__file__)


    try:
        arguments = parser.parse_args()
        command = arguments.command
        secret = arguments.secret
        public_key = arguments.public_key
        cli.dispatch(command, secret, public_key)
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(1)