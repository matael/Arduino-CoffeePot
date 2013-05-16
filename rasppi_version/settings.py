#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# settings.py

# Settings for twitter coffee pot system

# PLEASE DO NOT SHARE TOKENS


# coffee pot twitter API key
CONSUMER_KEY = ''

# coffee pot twitter api secret
CONSUMER_SECRET = ''

# API Token
TOKEN_KEY = ''

# Token  secret
TOKEN_SECRET = ''

# coffeepot's master twitter name
MASTER_NAME = u''

# pattern to start coffeepot
RE_START = re.compile('givemecoffee')

# pattern to stop coffeepot
RE_STOP = re.compile('thanksforcoffee')

# Time between 2 lookups for a tweet (seconds)
UPDATE_TIME = 30
