import sys
from datetime import datetime

import psycopg2


class Database:
    """
    Datenbank-Klasse
    """

    def __init__(self, host, dbname, username, password):
        self.host = host
        self.dbname = dbname
        self.username = username
        self.password = password
        self.conn, self.cur = None, None

    def name(self):
        return self.dbname

    def open_db(self):
        try:  # Datenbankfehler abfangen...
            self.conn = psycopg2.connect(
                "host=" + self.host + " dbname=" + self.dbname + " user=" + self.username + " password=" + self.password)
            self.cur = self.conn.cursor()
        except psycopg2.OperationalError as e:
            self.protocol('-- ' + str(e))
            sys.exit(1)

    def close_db(self):
        try:  # Datenbankfehler abfangen...
            self.cur.close()
            self.conn.close()
        except psycopg2.OperationalError as e:
            self.protocol('-- ' + str(e))
            sys.exit(1)

    def fetchall(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def fetchone(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def execute(self, sql):
        self.cur.execute(sql)
        self.conn.commit()
        return None

    def update(self, sql):
        self.cur.execute(sql)
        self.conn.commit()
        return None

    def insert(self, sql):
        self.cur.execute(sql)
        self.conn.commit()
        return None

    def protocol(self, text: str):
        log = open(self.dbname + '.log', 'a')
        log.write('-- ' + str(datetime.now()) + '\n')
        log.write(text + '\n')
        log.flush()
        log.close()

    def __str__(self):
        return f'{self.__class__.__name__}(\'{self.dbname}\')'

    def __repr__(self):
        return f'{self.__class__.__name__}(\'{self.host}\', \'{self.dbname}\', \'{self.username}\', \'######\')'


if __name__ == '__main__':
    patbef = Database('localhost', 'epz', 'postgres', 'postgres')
