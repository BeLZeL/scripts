# Quick description

myArduinoClock allows you to switch colors for child's awakening, with 3 leds :
* red : go to sleep
* orange : nearly wake up
* green : wake up

# Details

This code uses DS3231 to get date, time and day of week.

## On Startup

On startup, leds will flash to indicates you the current time :
* green : 1500 milliseconds (ack)
* red : one time between 10 and 20 hours, two times between 20 hours and 24 hours
* orange : one to ten times, if the current 'hour' finishes by one to ten
* green : 1500 milliseconds (ack)
* red : one to six times, if the current 'minute' starts by one to six
* orange : one to ten times, if the current 'minute' finishes by one to ten
* green : 1500 milliseconds (ack)

Example, it's 21h59 :
* green : 1500 milliseconds (ack)
* 2 x red : 2 x 500 milliseconds
* 1 x orange : 1 x 500 milliseconds
* green : 1500 milliseconds (ack)
* 5 x red : 5 x 500 milliseconds
* 9 x orange : 9 x 500 milliseconds
* green : 1500 milliseconds (ack)

## Morning

Monday, Tuesday, Thursday, Friday :
* red : before 7h00
* orange : bewteen 7h00 and 7h15
* green : after 7h15

Wednesday, Saturday, Sunday :
* red : before 8h00
* orange : bewteen 8h00 and 8h30
* green : after 8h30
