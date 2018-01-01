#!/usr/bin/env python3
# Shutdown Raspberry Pi

# Connect a wire from two last pins
# After 3 seconds, Raspberry Pi shutdowns

# sudo aptitude install python3-rpi.gpio
# Copy shutdown.py to /home/pi
# use this command
# sudo nano /etc/rc.local
# to add this line just before "exit 0"
# sudo python3 /home/pi/shutdown.py &

#-- IMPORTS -------------------------------------

import os
import time
import sys
from gpio_class import *

#-- CONST ---------------------------------------

WIRE = 7 # GPIO04 + 1 (3V3)

#-- LOOP ----------------------------------------
    
def myloop(self):
    self.print("\tmyloop debug")
    #print("\tmyloop normal")
    if self.is_on(WIRE):
        time.sleep(3)
        if self.is_on(WIRE):
            self.print("\texit")
            os.system('sudo poweroff')
            sys.exit()

#-- RUN -----------------------------------------

gpio = myGPIO(myloop, IN=[WIRE], verbose=0)

#-- EOD -----------------------------------------
