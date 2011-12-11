#!/usr/bin/env python2
#-*- encoding: utf-8 -*-
#
#       bridge.py
#
#       12/2011 Mathieu Gaborit <mat.gaborit@gmx.com>
#       License : WTFPL

import sys
import os
import twitter
import time
import re
import serial

#############################################
################# S E T U P #################
#############################################

consumer_key = ''                           # coffee pot twitter API key
consumer_secret = ''   # coffee pot twitter api secret
master_name = u''                                         # coffeepot's master twitter name
serial_port = "/dev/ttyACM0"                                    # port where arduino is reachable
re_start = re.compile('givemecoffee')                           # pattern to start coffeepot
re_stop = re.compile('thanksforcoffee')                         # pattern to stop coffeepot
update_time = 30                                                # Time between 2 lookups for a tweet

#############################################

def do_coffee(api, ser):
    """Must i send a signal to the coffee pot ?"""
    print(" Fonction DoCoffee...") # DEBUG
    mention = api.GetMentions()[:1]
    if mention[0].user._screen_name == master_name:
        if re_start.search(mention[0].text):
            print("Hey ! Let's make coffee !")
            ser.write('1')
            return 0
        elif re_stop.search(mention[0].text):
            print("Yeah ! Coffee's ready !")
            ser.write('0')
            return 0
    else:
        print("Waiting for a tweet...")
        return 0


def main():
    # let's create an instance of the api
    try:
        api = twitter.Api(consumer_key=consumer_key,\
                          consumer_secret=consumer_secret,\
                          access_token_key='87711832-0X6wvXnI8mxByu4PrxFO8XVa6uLyBgcLSA6jrXMw',\
                          access_token_secret='mNcosbbAkHtNubTztJuW9bjBArN60sTgcAUTm6dmX4')
        print("Connected to the twitter API")
    except:
        print("Failed to load twitter API")
    try:
        ser = serial.Serial(port=serial_port)
        print("Serial Connection opened...")
    except:
        print("Failed to load serial connection")
    print("Entering main loop....")
    while 1:
        do_coffee(api, ser)
        time.sleep(update_time)
    return 0

if __name__ == '__main__': main()

