#!/bin/bash
# ./git_graph.sh <path/repo>
# Results are stored in /tmp/results.png

function read_git_history()
{
    MASTER_DIR=.
    SUB_DIRS=.

    # Parse hash newer to older
    for hash in $(git log --format=%H ${MASTER_DIR})
    do
        echo $hash
    
        git checkout $hash
    
        # 2017-05-03 17:39:39 +0200 -> 2017-05-03 17:39:39
        commiter_date=$(git log -1 --format=%ci ${MASTER_DIR} | cut -d' ' -f-2)
    
        nb_lines=$(find ${SUB_DIRS} -type f \( ! -path ".git" ! -name .gitignore \) 2>/dev/null | wc -l)    
    
        echo "${commiter_date}|${nb_lines}|$hash" >> /tmp/res
    done
}

rm -f /tmp/res

cd $1
read_git_history .
git checkout master
cd -

# sort older to newer
sort -u /tmp/res -o /tmp/input.csv

gnuplot -e "dir='Results' ; datafile='/tmp/input.csv'; outputname='/tmp/results.png'" git_graph.g
