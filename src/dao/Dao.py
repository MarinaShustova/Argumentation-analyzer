import psycopg2


class Dao:
    def __init__(self):
        self.db_name = 'templates'
        self.db_user = 'postgres'
        self.db_password = 'abcd'
        self.db_host = 'localhost'

    def get_cursor(self):
        conn = psycopg2.connect(dbname=self.db_name, user=self.db_user,
                                password=self.db_password, host=self.db_host)
        return conn.cursor()