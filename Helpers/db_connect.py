import pymysql
import configparser
from os.path import join, dirname


config = configparser.ConfigParser()
config.read(join(dirname(__file__), 'config.cfg'))


class DBConnect:

    db = config['DB']['db']

    def __init__(self):
        pass

    def __connect(self):
        """
        Establish database connection
        :return: connection
        """

        host = config['DB']['host']
        port = int(config['DB']['port'])
        user = config['DB']['user']
        passwd = config['DB']['passwd']
        db = config['DB']['db']
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)

        return conn

    def select(self, query):
        """
        Performs SELECT SQL statement with provided query
        :param query: query
        :return: all rows
        """

        # create connection
        conn = self.__connect()
        cur = conn.cursor()

        # execute query
        cur.execute(query)
        result = cur.fetchall()

        all_rows = []
        for line in result:
            row = []
            for col in line:
                row.append(str(col))  # convert values into string
            all_rows.append(row)

        conn.close()  # closing db connection
        cur.close()  # closing cursor

        return all_rows

    def update(self, query):
        """
        Performs UPDATE SQL statement with provided query
        :param query: query
        :return: execution result
        """

        # create connection
        conn = self.__connect()
        cur = conn.cursor()

        # execute query
        result = cur.execute(query)
        conn.commit()

        conn.close()  # closing db connection
        cur.close()  # closing cursor

        return result
