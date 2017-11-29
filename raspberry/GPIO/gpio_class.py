#!/usr/bin/env python3
# Framework GPIO

#-- IMPORTS -------------------------------------

from __future__ import print_function
import builtins as __builtin__
import RPi.GPIO as GPIO
import time
import types

#-- FRAMEWORK -----------------------------------

class myGPIO:

    def print(self, *args, **kwargs):
        if self.is_verbose:
            return __builtin__.print(*args, **kwargs)
   
    # IN = read / OUT = write
    def __init__(self, func_loop, MODE=GPIO.BOARD, IN=[], OUT=[], loop_delay=1, verbose=0):
       
        #-- Run CONF --
        self.set_verbose(verbose) # must be first
        self.set_loop_delay(loop_delay)
       
        #-- Run SETUP --
        self.print("Setup:")
        self.set_mode(MODE)
        self.set_in(IN)
        self.set_out(OUT)

        #-- Run LOOP --
        self.print("Run -------------------- ")
        self.loop(func_loop)

    def __del__(self):
        self.print("Exit:")
        self.print("\tGPIO.cleanup()")
        GPIO.cleanup()

    #-- CONF ----------------

    def set_verbose(self, verbose):
        self.is_verbose = verbose
        self.print("verbose", verbose)

    def set_loop_delay(self, loop_delay):
        self.loop_delay=loop_delay
        self.print("\tset loop delay to", loop_delay)

    #-- SETUP --------------
   
    def set_mode(self, mode):
        self.print("\tGPIO.setmode("+str(mode)+")")
        GPIO.setmode(mode)
           
    def set_in(self, pins):
        for pin in pins:
            self.print("\tGPIO.setup("+str(pin)+", GPIO.IN, GPIO.PUD_DOWN)")
            GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)

    def set_out(self, pins):
        for pin in pins:
            self.print("\tGPIO.setup("+str(pin)+", GPIO.OUT)")
            GPIO.setup(pin, GPIO.OUT)

    #-- CHECK --------------

    def is_on(self,pin):
        self.print("\tGPIO.input("+str(pin)+") == GPIO.HIGH ?", GPIO.input(pin))
        return GPIO.input(pin) == GPIO.HIGH
   
    def is_off(self,pin):
        self.print("\treturn GPIO.input("+str(pin)+") == GPIO.LOW")
        return GPIO.input(pin) == GPIO.LOW

    def set_on(self,pin):
        self.print("\tGPIO.output("+str(pin)+",GPIO.HIGH)")
        GPIO.output(pin,GPIO.HIGH)

    def set_off(self,pin):
        self.print("\tGPIO.output("+str(pin)+",GPIO.LOW)")
        GPIO.output(pin,GPIO.LOW)

    #-- LOOP --------------
   
    #def _loop(self): # will be override by your own
        #print("empty loop")

    def loop(self, func_loop):
        try:
            # override with your own loop
            #if func_loop is not None:
                #self._loop = types.MethodType(func_loop, self)

            while True:
                time.sleep(self.loop_delay)
                self.print("loop:")
                func_loop(self)
        except KeyboardInterrupt as error:
            pass
        # finally:
            #print("GPIO.cleanup()")
