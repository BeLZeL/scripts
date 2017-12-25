#!/bin/bash
# ./cron_temperature.sh
source $(dirname $0)/check_remote_dir.sh                                                                                                                                                                                               

#-------------------------------------------------------------------------------

# récupération de la température ; on obtient ici une valeur à 5 chiffres sans virgules (ex: 44123) :
TEMP=$(cat /sys/class/thermal/thermal_zone0/temp)

# on divise alors la valeur obtenue par 1000, pour obtenir un résultat avec deux chiffres seulement (ex: 44) :
TEMP=$(($TEMP/1000))

date +"%Y|%m|%d|%H|%M|%S|$TEMP" >> ${REMOTE_DIR}/cron_temperature.log

#-------------------------------------------------------------------------------
