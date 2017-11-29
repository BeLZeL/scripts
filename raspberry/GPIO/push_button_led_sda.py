#!/usr/bin/env python3
# Push Button and Light LED

#-- IMPORTS -------------------------------------

import time
from gpio_class import *

#-- CONST ---------------------------------------

BUTTON = 3 # GPIO22 + 3V3
LEDPIN = 11 # GPIO17 + GND

#-- LOOP ----------------------------------------
    
def myloop(self):
	if self.is_off(BUTTON):
		GPIO.output(LEDPIN,GPIO.HIGH)
	else:
		GPIO.output(LEDPIN,GPIO.LOW)

#-- RUN -----------------------------------------

gpio = myGPIO(myloop, IN=[BUTTON], OUT=[LEDPIN], loop_delay=.1, verbose=1)

#-- EOD -----------------------------------------