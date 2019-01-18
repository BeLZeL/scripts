Manage bash redirections

#------------------------------------------------------------------------------
# script with stdout and stderr

$ cat test.sh
#!/bin/bash
echo stdout
echo stderr >&2


#------------------------------------------------------------------------------
# Catch everything

$ ./test.sh 
stdout
stderr

$ ./test.sh 2>&1
stdout
stderr


#------------------------------------------------------------------------------
# Catch one

$ ./test.sh 2> /dev/null
stdout

$ ./test.sh > /dev/null
stderr


#------------------------------------------------------------------------------
# Catch nothing

# Error ! stderr is redirected to stdout, then stdout is filtered
$ ./test.sh 2>&1 > /dev/null
stderr

# Good ! stdout is filtered, then stderr is redirected to stdout (and filtered too)
$ ./test.sh > /dev/null 2>&1

# Also Good ! stdout and stderr are filtered (not working everywhere)
$ ./test.sh &> /dev/null
