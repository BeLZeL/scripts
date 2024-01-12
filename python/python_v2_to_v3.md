Python2                           -> python3
--------------------------------------------------------------
#!/usr/bin/env python             -> #!/usr/bin/env python3 or #!/usr/bin/python3
dict.iteritems()                  -> dict.items()                           |
import module                     -> import directory.module                |
string                            -> bytes.decode('utf-8')                  | TypeError: a bytes-like object is required, not 'str' / TypeError: cannot use a string pattern on a bytes-like object
bytes                             -> string.encode('utf-8')                 | TypeError: Unicode-objects must be encoded before hashing
import urllib                     -> import urllib.request                  |
from StringIO import StringIO     -> from io import StringIO                |
len(map(str,range(10)))           -> len(list(map(str,range(10))))          |
psycopg2.ProgrammingError.message -> psycopg2.ProgrammingError.args         |
data = conn.recv(4096)            -> data = conn.recv(4096).decode('utf-8') |
