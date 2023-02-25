import psycopg2
from datetime import datetime
import sys


class Database:
    """
    Datenbank-Klasse
    """

    def __init__(
        self,
        host = 'localhost',
        dbname = 'epz',
        username = 'postgres',
        password = 'postgres'
    ):
        self.conn = None
        self.cur = None

        self.pg_connection_dict = {
            'dbname': dbname,
            'host': host,
            'user': username,
            'password': password
        }

    def name(self):
        return self.pg_connection_dict[dbname]

    def open_db(self):
        try:  # Datenbankfehler abfangen...
            self.conn = psycopg2.connect(**self.pg_connection_dict)
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
        log = open(f'{self.pg_connection_dict[dbname]}.log', 'a')
        log.write('-- ' + str(datetime.now()) + '\n')
        log.write(text + '\n')
        log.flush()
        log.close()
