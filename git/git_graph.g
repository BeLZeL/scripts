#! /usr/bin/gnuplot
# Called directly by git_graph.sh
# gnuplot -e "datafile='/tmp/input.csv'; outputname='git_graph.png'" git_graph.g

set title sprintf("Number of Files for %s", dir)
set timefmt "%Y-%m-%d %H:%M:%S"
set xdata time
set xtics nomirror rotate by -270 
set format x "%Y-%m"
set terminal png size 800,600 enhanced font "Helvetica,10"
set output outputname
set datafile separator "|"
plot datafile using 1:2 with line title ''
