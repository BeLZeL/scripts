aptitude install sqlite3 libsqlite3-dev

#------------------------------------------------------------------------------
# https://www.sitepoint.com/getting-started-sqlite3-basic-commands/
sqlite3 example.db
sqlite> .help

#------------------------------------------------------------------------------
# Storage Classes and Datatypes
* NULL. The value is a NULL value.
* INTEGER. The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
* REAL. The value is a floating point value, stored as an 8-byte IEEE floating point number.
* TEXT. The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).
* BLOB. The value is a blob of data, stored exactly as it was input.
* BOOL does NOT exists -> use INTEGER instead

#------------------------------------------------------------------------------
# https://docs.python.org/3.5/library/sqlite3.html
sqlite> CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real);
sqlite> INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)
sqlite> select * from stocks;
date|trans|symbol|qty|price
2006-01-05|BUY|RHAT|100.0|35.14

#------------------------------------------------------------------------------
# Pretty print
sqlite>.mode column
sqlite>.headers on
sqlite>.width <a> <b> ... <z>

#------------------------------------------------------------------------------
# List of tables
sqlite> .tables : list of tables

#------------------------------------------------------------------------------
# Schema of a table
sqlite> .schema
CREATE TABLE recipes ( name text, version text, username text, channel text);
CREATE TABLE packages ( id text, fullname text);
sqlite> .schema recipes
CREATE TABLE recipes ( name text, version text, username text, channel text);
