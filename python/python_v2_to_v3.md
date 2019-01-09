Python2                           -> python3
--------------------------------------------------------------
dict.iteritems()                  -> dict.items()
import module                     -> import directory.module
string                            -> bytes.decode('utf-8')
bytes                             -> string.encode('utf-8')
import urllib                     -> import urllib.request
from StringIO import StringIO     -> from io import StringIO
len(map(str,range(10)))           -> len(list(map(str,range(10))))
psycopg2.ProgrammingError.message -> psycopg2.ProgrammingError.args
data = conn.recv(4096)            -> data = conn.recv(4096).decode('utf-8')
