#!/bin/bash

# If uptime is lower than "valid_time_between_restart" in seconds, so it fails
#   From   0 minute  to   2 minutes -> restart each 10 seconds
#   From   2 minutes to  15 minutes -> restart each 30 seconds
#   From  15 minutes to 120 minutes -> restart each  1 minute
#   From 120 minutes                -> restart each 10 minutes
# If uptime is greater than "valid_time_between_restart" in seconds, so it's ok
#   Reinit counters

        
nb_restarts=0
valid_time_between_restart=15

date

while [ true ]
do

    # Init datetime and try to launch the process
    dt_process_start=$(date +%s)    
    if [ $(( $RANDOM % 20 )) == 0 ]
    then
        echo "RUN RUN RUN"
        sleep $(( valid_time_between_restart + 1 ))
        date
    fi
    
    # Compute uptime of process
    dt_process_end=$(date +%s)
    diff=$(( dt_process_end - dt_process_start ))
    
    # If uptime is lower than "valid_time_between_restart" in seconds, so it fails
    # Do a progress sleep between restarts
    if [ ${diff} -lt ${valid_time_between_restart} ]
    then
        nb_restarts=$(( nb_restarts + 1 ))
          if [ ${nb_restarts} -lt  12 ]; then echo "$(date) ${nb_restarts} -> sleep  10"; sleep  10;    #  12 times, length  120 seconds, from   0 minute  to   2 minutes (restart each 10 seconds)
        elif [ ${nb_restarts} -lt  38 ]; then echo "$(date) ${nb_restarts} -> sleep  30"; sleep  30;    #  26 times, length  780 seconds, from   2 minutes to  15 minutes (restart each 30 seconds)
        elif [ ${nb_restarts} -lt 155 ]; then echo "$(date) ${nb_restarts} -> sleep  60"; sleep  60;    # 105 times, length 6300 seconds, from  15 minutes to 120 minutes (restart each  1 minute)
        else                                  echo "$(date) ${nb_restarts} -> sleep 600"; sleep 600; fi # unlimited times and length,     from 120 minutes                (restart each 10 minutes)
        
    # If uptime is greater than "valid_time_between_restart" in seconds, so it's ok
    # Reset counters
    else
        nb_restarts=0
    fi

done
