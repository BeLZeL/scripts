#!/usr/bin/env python3
 
# SQL
import select
import psycopg2
import psycopg2.extensions
from sqlalchemy import create_engine, text

# OTHERS
import datetime

def do_request(conn, request, logresult=False):
    print(datetime.datetime.now(), "SQL ->", request)
    try:
        res = conn.execute(text(request).execution_options(autocommit=True))
        if request.startswith("update") or logresult == True:
            print(datetime.datetime.now(), "SQL <-", "returns_rows =", res.returns_rows, "rowcount =", res.rowcount)
        return res
    except:
        print(datetime.datetime.now(), "Unexpected error/exception:", sys.exc_info())
        return [ ]


db_conn    = create_engine("postgresql+psycopg2://<user>@<host>/<db>").connect()
db_results = do_request(db_conn, "select id from table;")
for db_line in sorted(db_results):
    db_line_items = dict(db_line.items())
    print(db_line_items)
    print(db_line_items['id'])
