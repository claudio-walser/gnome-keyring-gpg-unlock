CLI Commands
============

Encrypt a file
gpg --output secret --encrypt --recipient E51D8637C4F97C850BC97BF55638393858B04300  secret.clear && rm -rf secret.clear

Decrypt a file
gpg --quiet --decrypt secret

Decrypt and unlock
gpg --quiet --decrypt secret | gnome-keyring-daemonm -r --unlock




Credits
=======

- Idea
The idea about gpg encrypt your password and unlock the gnome-keyring with it, has been successfully stolen from recolic
https://github.com/recolic/gnome-keyring-yubikey-unlock
