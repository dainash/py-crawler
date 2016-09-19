"""
mysql only use for store parsed web page data
only supply create api,search api
"""
import mysql.connector


class MysqlDB(object):
    def __init__(self):
        config = {
            'user': 'root',
            'password': '297279',
            'host': '127.0.0.1',
            'database': 'baike',
            'raise_on_warnings': True
        }
        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor()

    def insert(self, value):
        addData = ("INSERT INTO page_data "
                   "(title, img, description, `index`) "
                   "VALUES (%s, %s, %s, %s)")
        self.cursor.execute(addData, value)

        self.cnx.commit()
        self.cnx.close()

    def getLast(self):
        getLastData = ("select `index` from page_data order by id DESC limit 1")
        self.cursor.execute(getLastData)
        last_one = self.cursor.fetchone()
        self.cnx.commit()
        self.cnx.close()
        return last_one
