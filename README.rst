Why
===

There are a few reasons, why you would want to unlock your keyring automatically. I don't judge, everybody has her/his own reasons. Enabled autologin is one you find very often. But also headless systems without gnome-session handling, you still want to store your secrets safely I guess.

I personally use a yubikey and decided a challenge-response is sufficient for my login. Also, I do have a GPG keypair, which is also stored on the yubikey.
The private key on the yubikey is protected through a pin. After 3 pin mismatches the private keys get deleted from the yubikey.
Of course i do store password encrypted backups of my private keys within a encrypted database of a local password manager.

Long story short, I do this because I don't want to type in my utterly long password everytime I log into the device. But, I also don't want to sacrifice security. 

The idea is to store your password of the default gnome-keyring gpg-encrypted on your disk. This is fine for me with a yubikey, where the private keys aren't loaded in the system the whole time. I can un-plug my yubikey which effectively prevents my system from decrypting anything. With my private keys sitting in my .gnupg directory and beeing unlocked permanentely, I would not be that confident with this solution.

Then also, gnome-keyring uses by default your user password for the default keyring. This makes sense, regarding the fact, your system unlocks the default keyring after login using your given password.
In this setup, I recommend using a different, unique password for your default keyring. You can change the keyrings password with seahorse, for example.

.. container:: alert alert-warning

    **One other "solution" you come across frightening often while searching for a solution: Use an empty password for your default keyring. DON'T DO THIS! This is the worst idea, better don't use gnome-keyring at all then.**



Setup
=====

.. code-block:: bash

    pip install --user --upgrade gnome-keyring-gpg-unlock
    gnome-keyring-gpg-unlock setup --public-key <your-gpg-public-key> --secret <path-where-your-encrypted-password-is-stored>

Type in your keyring password when asked. 


Check Setup
===========
Check your password
.. code-block:: bash

    gpg --quiet --decrypt <path-where-your-encrypted-password-is-stored>

Check the service file
.. code-block:: bash

    systemctl --user cat gnome-keyring-gpg-unlock.service

Check unlock
Lock your default keyring in seahorse.
.. code-block:: bash

    gnome-keyring-gpg-unlock unlock --secret <path-where-your-encrypted-password-is-stored>

Seahorse won't update it's ui, press the unlock button and the secrets will appear without a login prompt. Or close and reopen seahorse.


Credits
=======

- Idea
The whole idea of this is not mine. I have seen it first at recolic's repository. Unfortunately i had issues compiling his project. So i deciced to take the (for me) simpler approach and rewrite it as a python package.
https://github.com/recolic/gnome-keyring-yubikey-unlock

- Unlock the keyring
There is a controversial debate going on about this. Libsecret does not provide an api for unlocking keyrings by password directly. For security reasons, they decided to only unlock via a password dialog under all circumstances. The same goes for the python module keyring. Håvard Moen solved this by interacting with the gnome-keyring control socket directly. You might want to look into his approach using the tpm chip anyway.
https://codeberg.org/umglurf/gnome-keyring-unlock
