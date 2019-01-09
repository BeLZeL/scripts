parallel allows to launch multiple processes.

#------------------------------------------------------------------------------
# Date

$ parallel 'date +"%F %T number={1}, unit={2}"' ::: 1 3 5 7 ::: minute hour
2019-01-08 15:31:25 number=1, unit=minute
2019-01-08 15:31:25 number=1, unit=hour
2019-01-08 15:31:25 number=3, unit=minute
2019-01-08 15:31:25 number=3, unit=hour
2019-01-08 15:31:25 number=5, unit=minute
2019-01-08 15:31:25 number=5, unit=hour
2019-01-08 15:31:25 number=7, unit=minute
2019-01-08 15:31:25 number=7, unit=hour

#------------------------------------------------------------------------------
# Sleep + date

$ parallel 'sleep {1} && date +"%F %T number={1}, unit={2}"' ::: 1 3 5 7 ::: minute hour
2019-01-08 15:31:49 number=1, unit=minute
2019-01-08 15:31:49 number=1, unit=hour
2019-01-08 15:31:51 number=3, unit=minute
2019-01-08 15:31:51 number=3, unit=hour
2019-01-08 15:31:53 number=5, unit=minute
2019-01-08 15:31:53 number=5, unit=hour
2019-01-08 15:31:55 number=7, unit=minute
2019-01-08 15:31:55 number=7, unit=hour

#------------------------------------------------------------------------------
# Use parallel -j to launch more than 8 processes.

$ parallel 'sleep {1} && date +"%F %T number={1}, unit={2}"' ::: 1 3 5 7 ::: minute hour days
2019-01-08 15:30:18 number=1, unit=minute
2019-01-08 15:30:18 number=1, unit=hour
2019-01-08 15:30:18 number=1, unit=days
2019-01-08 15:30:20 number=3, unit=minute
2019-01-08 15:30:20 number=3, unit=hour
2019-01-08 15:30:20 number=3, unit=days
2019-01-08 15:30:22 number=5, unit=minute
2019-01-08 15:30:22 number=5, unit=hour
2019-01-08 15:30:23 number=5, unit=days
2019-01-08 15:30:25 number=7, unit=minute
2019-01-08 15:30:25 number=7, unit=hour
2019-01-08 15:30:27 number=7, unit=days

$ parallel -j 1000 'sleep {1} && date +"%F %T number={1}, unit={2}"' ::: 1 3 5 7 ::: minute hour days
2019-01-08 15:30:39 number=1, unit=minute
2019-01-08 15:30:39 number=1, unit=hour
2019-01-08 15:30:39 number=1, unit=days
2019-01-08 15:30:41 number=3, unit=minute
2019-01-08 15:30:41 number=3, unit=hour
2019-01-08 15:30:41 number=3, unit=days
2019-01-08 15:30:43 number=5, unit=minute
2019-01-08 15:30:43 number=5, unit=hour
2019-01-08 15:30:43 number=5, unit=days
2019-01-08 15:30:45 number=7, unit=minute
2019-01-08 15:30:45 number=7, unit=hour
2019-01-08 15:30:45 number=7, unit=days

#------------------------------------------------------------------------------
# Show a quick summary with a bar
$ parallel --bar 'echo "number={1}, unit={2}" > /dev/null' ::: 1 3 5 7 ::: minute hour
