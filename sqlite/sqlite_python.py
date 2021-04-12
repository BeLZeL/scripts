#!/usr/bin/env python3
# aptitude install sqlite3 libsqlite3-dev
# https://docs.python.org/3.5/library/sqlite3.html

import sqlite3

def create_db():
    conn = sqlite3.connect('conan.db')
    c = conn.cursor()

    c.execute("SELECT name FROM sqlite_master WHERE type='table' and name='recipes';")
    if len(c.fetchall()) == 0:
        c.execute("CREATE TABLE recipes ( name text, version text, username text, channel text)")

    c.execute("SELECT name FROM sqlite_master WHERE type='table' and name='packages';")
    if len(c.fetchall()) == 0:
        c.execute("CREATE TABLE packages ( id text, fullname text)")

    c.execute("DELETE FROM recipes")
    c.execute("DELETE FROM packages")

    conn.commit()
    conn.close()

def insert(self):
    conn = sqlite3.connect('conan.db')
    c = conn.cursor()

    c.execute('INSERT INTO recipes VALUES (?, ?, ?, ?)', (self.name, recipe.version, recipe.username, recipe.channel))

    conn.commit()
    conn.close()
