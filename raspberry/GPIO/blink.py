#!/usr/bin/env python3
# Blink PIN11/ GPIO17 50 times

#-- IMPORTS -------------------------------------

import time
from gpio_class import *

#-- CONST ---------------------------------------

LEDPIN = 11 # GPIO017 + GND

#-- LOOP ----------------------------------------

# blinking function
def blink(self,pin):
	self.set_on(pin)
	time.sleep(1)
	self.set_off(pin)
	time.sleep(1)
	return

def myloop(self):
	for i in range(0,50):
		blink(self,LEDPIN)

#-- RUN -----------------------------------------

gpio = myGPIO(myloop, OUT=[LEDPIN], verbose=1)

#-- EOD -----------------------------------------