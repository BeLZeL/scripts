#!/usr/bin/python

import sys
import re
import subprocess

print sys.argv[1]

# readelf - Displays information about ELF files.
# Note: the =decodedline option will display the interpreted contents of a .debug_line section whereas the =rawline option dumps the contents in a raw format.
result = subprocess.check_output("readelf --debug-dump=decodedline %s" % ( sys.argv[1]), shell=True)

addresses = { }
for line in result.splitlines():
    m = re.search('([^ ]*)\s*([^ ]*)\s*(0x.*)', line)
    if m is not None:
        file = m.group(1)
        line = m.group(2)
        address = m.group(3)
        #print address + " <=> " + file + "@" + line
        addresses[address] = file+"@"+line
    #else:
        #print line.rstrip()

for line in sys.stdin:
    m = re.search('.* \[(?P<address>0x.*)\]', line)
    if m is not None:
        found = 0
        max_address = int(m.group('address'), 0)
        
        # Try range before address founded
        for address in range(max_address - 8, max_address - 1):
            #print "try " + str(hex(address))
            if hex(address) in addresses:
                print m.group(0) + " <=== " + addresses[hex(address)]
                found = 1
                break

        if found == 0:
            print m.group(0) + " <=== not found"
    else:
        print line.rstrip()
