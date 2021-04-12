#!/usr/bin/env python3

'''
===============================================================================
$ ./try_argparse.py 
usage: try_argparse.py [-h] [-d] -c CONF [-o OUTPUT_VAR] [-n [NUMBER]]
try_argparse.py: error: the following arguments are required: -c/--conf
-------------------------------------------------------------------------------
$ ./try_argparse.py --help
usage: try_argparse.py [-h] [-d] -c CONF [-o OUTPUT_VAR] [-n [NUMBER]]

Generate HELP

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Turn on debug informations.
  -c CONF, --conf CONF
  -o OUTPUT_VAR, --output OUTPUT_VAR
  -n [NUMBER], --number [NUMBER]
===============================================================================
$ ./try_argparse.py -c 'file.conf'
file.conf
set by default : None
set by default : None
-------------------------------------------------------------------------------
$ ./try_argparse.py -dc 'file.conf'
debug
file.conf
set by default : None
set by default : None
-------------------------------------------------------------------------------
$ ./try_argparse.py -c 'file.conf' -o output
file.conf
set by user : output
set by default : None
-------------------------------------------------------------------------------
$ ./try_argparse.py -c 'file.conf' -n
file.conf
set by user : output
set by user : 1
-------------------------------------------------------------------------------
$ ./try_argparse.py -c 'file.conf' -n 3
file.conf
set by user : output
set by user : 3
===============================================================================
'''

if __name__ == '__main__':
    from argparse import ArgumentParser

    args = ArgumentParser(description="Generate HELP")
    args.add_argument("-d", "--debug", help='Turn on debug informations.', action='store_true')
    args.add_argument("-c", "--conf", default=None, required=True)
    args.add_argument("-o", "--output", dest='output_var', default=None)
    args.add_argument("-n", "--number", nargs='?', const=1, type=int)
    options = args.parse_args()

    if options.debug:
        print('debug')
    
    print(options.conf)
    
    if options.output_var:
        print("set by user :", options.output_var)
    else:
        print("set by default :", options.output_var)

    if options.number:
        print("set by user :", options.number)
    else:
        print("set by default :", options.number)
