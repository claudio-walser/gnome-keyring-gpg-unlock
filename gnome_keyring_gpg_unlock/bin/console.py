#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import sys
import argcomplete
import argparse


# create parser in order to autocomplete
parser = argparse.ArgumentParser()

parser.add_argument(
    "command",
    help="Command to call.",
    type=str,
    choices=[
        'init',
        'clean',
        'start',
        'test',
        'review',
        'finish',
        'release',
        'status',
        'compare',
        'upgrade',
        'refresh',
        'version'
    ]
    #choices=cli.getAvailableCommands()
)
# parser.add_argument(
#     "branch",
#     help="Your awesome feature-branch name",
#     type=str
# )
argcomplete.autocomplete(parser)


def main():

    try:
        arguments = parser.parse_args()
        print(f'Execute {arguments.command}')
        # command = arguments.command
        # branch = arguments.branch
        # cli.dispatch(command, branch)
        # sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(1)