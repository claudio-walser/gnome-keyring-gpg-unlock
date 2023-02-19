#!/usr/bin/env python3

from setuptools import setup, find_packages


def read(fpath):
    with open(fpath, 'r') as f:
        return f.read()


def version(fpath):
    return read(fpath).strip()


setup(
    name='gnome_keyring_gpg_unlock',
    version=version('version.txt'),
    description='Auto unlock your default gnome-keyring with a gpg encrypted password',
    long_description=read('README.rst'),
    author='Claudio Walser',
    author_email='info@gitcd.io',
    url='https://github.com/claudio-walser/gnome-keyring-gpg-unlock',
    packages=find_packages(),
    install_requires=[
        'simpcli',
        'python-gnupg',
        'argparse',
        'argcomplete',
        'typing'
    ],

    entry_points={
        'console_scripts': [
            'gnome-keyring-gpg-unlock = gnome_keyring_gpg_unlock.bin.console:main',
        ]
    },
    license='Apache License',
    keywords=['keyring', 'gnome-keyring', 'unlock', 'gnome-keyring-unlock'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Security'
    ]
)