#!/usr/bin/env python

import sys

from src.Secret import Secret
from src.Keyring import Keyring

publicKey = 'E51D8637C4F97C850BC97BF55638393858B04300'

secret = Secret(publicKey)
keyringPassword = secret.decrypt('/home/claudio/.sec/secret')

keyring = Keyring()
keyring.unlock(keyringPassword)

sys.exit(0)
