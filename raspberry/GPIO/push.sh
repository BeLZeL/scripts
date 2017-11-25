#!/bin/bash

./GPIO_in.sh $1

while true
do
  until grep 1 /sys/class/gpio/gpio$1/value >> /dev/null
  do
    sleep .1
  done
  
  echo "Push"
done
