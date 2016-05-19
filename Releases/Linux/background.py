#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import platform
import time
from ctypes import CDLL

def get_steam_api():
    if sys.platform.startswith('linux'):
        if platform.architecture()[0].startswith('32bit'):
            print('Loading Linux 32bit library')
            steam_api = CDLL('./libsteam_api32.so')
        elif platform.architecture()[0].startswith('64bit'):
            print('Loading Linux 64bit library')
            steam_api = CDLL('./libsteam_api64.so')
        else:
            print('Linux architecture not supported')
            sys.exit()
    else:
        print('OS not supported')
        sys.exit()

    return steam_api

if __name__ == '__main__':
    delay = 60*60*24*7

    if len(sys.argv) != 2:
        print("Wrong number of arguments")
        sys.exit()

    str_app_id = sys.argv[1]

    os.environ["SteamAppId"] = str_app_id

    try:
       get_steam_api().SteamAPI_Init()
       time.sleep(delay)
    except:
        print("Couldn't initialize Steam API")
