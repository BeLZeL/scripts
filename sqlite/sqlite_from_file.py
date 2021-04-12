#!/usr/bin/env python3
# aptitude install sqlite3 libsqlite3-dev
# https://docs.python.org/3.5/library/sqlite3.html

import re
import os
import sqlite3

dbname='local'
filename='input'

#---------------------------------

def create_db(table):
    conn = sqlite3.connect(dbname + '.db')
    c = conn.cursor()

    try:
        c.execute("CREATE TABLE " + table + " ( id text, code text, foo text, bar text, manual text )" )
    except sqlite3.OperationalError as e:
        c.execute("DELETE FROM " + table )

    conn.commit()
    conn.close()

def insert(table, values):
    conn = sqlite3.connect(dbname + '.db')
    c = conn.cursor()

    c.execute('INSERT INTO ' + table + ' VALUES (?, ?, ?, ?, ?)', (values[0], values[1], values[2], values[3], values[4]))

    conn.commit()
    conn.close()

#---------------------------------

create_db(filename)

# A|B|C|D|E
fichier=open("/tmp/" + filename + ".txt", "r")
for line in fichier.readlines():
    line = line.rstrip()
    parsed = line.split('|')
    print(line + "\t======> " + parsed[0] )
    insert(filename, parsed)
fichier.close()

