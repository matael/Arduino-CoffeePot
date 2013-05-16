#! /bin/bash
#
# rpi_setup.sh
# Author: Matael

# Setup python package for tweeting coffeePot

# update distribute (RPi.GPIO requires last version)
easy_install -U distribute || easy_install-2.7 -U distribute

# because it's *much* better
easy_install -U pip || easy_install-2.7 -U pip

pip install python-twitter RPi.GPIO OAuth2

echo "This script will upgrade/install : distribute, pip, twitter, RPi.GPIO"


