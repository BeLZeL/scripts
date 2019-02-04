#!/usr/bin/env python3

'''
$ ./try_argparse.py 
usage: try_argparse.py [-h] [-d] -c CONF
try_argparse.py: error: the following arguments are required: -c/--conf

$ ./try_argparse.py --help
usage: try_argparse.py [-h] [-d] -c CONF

Generate HELP

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Turn on debug informations.
  -c CONF, --conf CONF

$ ./try_argparse.py -c 'file.conf'
file.conf

$ ./try_argparse.py -dc 'file.conf'
debug
file.conf
'''

if __name__ == '__main__':
    from argparse import ArgumentParser

    args = ArgumentParser(description="Generate HELP")
    args.add_argument("-d", "--debug", help='Turn on debug informations.', action='store_true')
    args.add_argument("-c", "--conf", default=None, required=True)
    options = args.parse_args()

    if options.debug:
        print('debug')
    
    print(options.conf)
