#!/usr/bin/env python3
# Blink PIN11/ GPIO17 50 times

import RPi.GPIO as GPIO
import time

MODE=GPIO.BOARD # or MODE=GPIO.BCM
PIN=11 # or PIN=17

def setup():
	# Use Raspberry Pi board pin numbers
	GPIO.setmode(MODE)
	# set up GPIO output channel
	GPIO.setup(PIN, GPIO.OUT)

# blinking function
def blink(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(1)
	return

# call blink 50 times	
def loop():
	for i in range(0,50):
		blink(PIN)

try:
	setup()
	loop()
except:
	pass
GPIO.cleanup()
