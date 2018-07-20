import pymysql

# DB Name
db = 'wp906'

class DBConnect:

    def __init__(self):
        pass

    def __connect(self, db):
        """

        :param db:
        :return:
        """

        host = '127.0.0.1'
        conn = pymysql.connect(host=host, port=3306, user='root', passwd='mysql', db=db)

        return conn

    def select(self, db, query):
        """

        :param db:
        :param query:
        :return:
        """

        # create connection
        conn = self.__connect(db)
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

    def update(self, db, query):
        """

        :param db:
        :param query:
        :return:
        """

        # create connection
        conn = self.__connect(db)
        cur = conn.cursor()

        # execute query
        result = cur.execute(query)
        conn.commit()

        conn.close()  # closing db connection
        cur.close()  # closing cursor

        return result
