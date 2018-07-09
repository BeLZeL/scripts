#!/usr/bin/env python3

'''
$ ./read_file.py 
#!/usr/bin/env python3

'''

def read_file(file):
    try:           
        with open(file, 'r') as f:
            line = f.readline()
            print(line)
    except Exception as e:
        raise Exception('On a une erreur') from e

read_file('read_file.py')
