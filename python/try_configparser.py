#!/usr/bin/env python3
'''
$ ./try_configparser.py ; cat /tmp/file.conf
[product]
key = value
'''

import configparser # aptitude install python-configparser
   
file='/tmp/file.conf'

config = configparser.ConfigParser()
config.read(file)

if 'product' not in config:
    config['product'] = {}

with open(file, 'w') as configfile:
    config['product']['key'] = 'value'
    config.write(configfile)
