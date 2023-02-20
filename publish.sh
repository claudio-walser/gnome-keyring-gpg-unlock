#!/bin/bash

rm -rf dist/ build/ *.egg-info/
python setup.py bdist_wheel
twine upload dist/*
