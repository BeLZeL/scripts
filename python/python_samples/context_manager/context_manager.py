# TODO

class db_open:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.connector = None

    def __enter__(self):
        self.connector = db_connect(self.host, self.user, self.password

    def __exit__(self, type, value, traceback):
        if (type is None) and (value is None) and (traceback is None):
            db_commit()
        else
            db_rollback()
        db_disconnect()
