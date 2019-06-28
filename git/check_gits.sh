#!/bin/bash

for master_dir in ~/workspace1 ~/workspace2
do
    for dir in $(find ${master_dir} -mindepth 1 -maxdepth 1 -type d)
    do
        res=$(cd ${dir} && git status --porcelain 2>/dev/null | sed 's/$/<br>/g')
        [ -z "${res}" ] && color=green || color=red
        res_ls=$(cd ${dir} && grep "<name>" .project 2>/dev/null | grep -v managedbuilder | sed 's/\s*<name>\(.*\)<\/name>/\1/g')
        [ -z "${res_ls}" ] && eclipse="" || eclipse=" (eclipse -> ${res_ls})"
        echo -e "<font color=${color}>${dir}</font>${eclipse}<br>${res}<br><br>"
    done
done | mail -a "Content-type: text/html" -s "[LOCAL] Check Gits" <mail>
