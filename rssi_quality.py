#!/usr/bin/python
# coding: utf-8

##
## testing things that could be used in Python 3.x

# import colorama
# colorama.init()
#
# dBm = "\033[1;33m"     # yellow bold | decibel-milliwatts
# '%  = "\033[1;34m"     # blue bold   | signal percentage
# '≠','=' = "\033[1;33m" # yellow bold | ≠ / = (NOT EQUAL TO and EQUAL signs)
# 
#
# below code is for Python 2.x
#


class bcolor:
    UNS = '\033[1;41m'
    LOW = '\033[1;31m'
    MEDIUM = '\033[1;34m'
    HIGH = '\033[1;32m'
    ERR = '\033[1;35m'
    ENDC = '\033[0;m'

import os
cmd = "iwconfig wlp3s0 | grep Signal | /usr/bin/awk '{print $4}' | /usr/bin/cut -d'=' -f2"
strDbm = os.popen(cmd).read()
if (strDbm):
    dbm = int(os.popen(cmd).read())
    quality = 2 * (dbm + 100)
    print ('\n\033[1;37m   [ RSSI Quality Guide ]  \033[0;m\n')
    print ('-96dBm ≠ 8 %'  '\t\033[1;37;41m[ Unusable ]\033[0;m')
    print ('-85dBm ≠ 30%'  '\t\033[1;31m[ Low ]\033[0;m')
    print ('-75dBm ≠ 50%'  '\t\033[1;34m[ Medium ]\033[0;m')
    print ('-55dBm ≠ 90%'  '\t\033[1;32m[ High ]\033[0;m')
    print('\n\033[1;33mCurrent:\033[0;m \033[1;34m{0}\033[0;m\033[1;33mdBm =\033[0;m \033[1;34m{1}%\033[0;m\n'.format(dbm, quality))
else:
    print (bcolor.ERR + ('Not in range or no Wi-Fi signal.') + bcolor.ENDC)
