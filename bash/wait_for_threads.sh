#!/bin/bash

num=0
for i in $(seq 1 16)
do
    bash -c "sleep ${i} ; echo \"${i}\"" &
    
    pids[$num]=$!
    num=$(( $num + 1 ))
done

echo "wait"
for pid in ${pids[*]}; do
    wait $pid
done
echo "end"
