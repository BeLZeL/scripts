#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Shutdown and restart."""

import os
import time
import sys

import RPi.GPIO as GPIO


BUTTON = 15 # + GND
LEDPIN = 11 # + GND


def set_in_pins(pins):
    """Setup pins as input."""
    for pin in pins:
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)
	GPIO.setup(LEDPIN, GPIO.OUT)
	GPIO.output(LEDPIN, GPIO.LOW)


def is_on(pin):
    """Check if pin is on."""
    return GPIO.input(pin) == GPIO.HIGH


try:
    GPIO.setmode(GPIO.BOARD)

    set_in_pins([BUTTON])

    while True:
		time.sleep(.1)
		if is_on(BUTTON):
			time.sleep(3)
			if is_on(BUTTON):
				GPIO.output(LEDPIN,GPIO.HIGH)
				time.sleep(3)
				GPIO.output(LEDPIN,GPIO.LOW)
				time.sleep(3)
				print('sudo poweroff')
				sys.exit()
			else:
				GPIO.output(LEDPIN,GPIO.HIGH)
				time.sleep(1)
				GPIO.output(LEDPIN,GPIO.LOW)
				time.sleep(1)
				print('sudo reboot')
				sys.exit()

except KeyboardInterrupt as error:
    pass

finally:
    GPIO.cleanup()
