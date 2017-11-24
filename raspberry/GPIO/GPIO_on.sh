#!/bin/bash
[ -d /sys/class/gpio/gpio$1 ] ||
	echo $1 > /sys/class/gpio/export
[ -w /sys/class/gpio/gpio$1/direction ] && {
	echo out > /sys/class/gpio/gpio$1/direction
	echo 1 > /sys/class/gpio/gpio$1/value
	echo -n "GPIO$1="; cat /sys/class/gpio/gpio$1/value
}
