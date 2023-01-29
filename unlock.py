#!/usr/bin/env python

import sys

from src.Secret import Secret
from src.Keyring import Keyring


secret = Secret()
keyringPassword = secret.decrypt('/home/claudio/.sec/gnome-keyring')

keyring = Keyring()
keyring.unlock(keyringPassword)

sys.exit(0)
