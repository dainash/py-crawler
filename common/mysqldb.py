"""
mysql only use for store parsed web page data
only supply create api,search api
"""
import mysql.connector
import ConfigParser

class MysqlDB(object):
    def __init__(self):
        cf = ConfigParser.ConfigParser()
        cf.read('conf/db.conf')

        user = cf.get('common', 'db_user')
        password = cf.get('common', 'db_pswd')
        host = cf.get('common', 'db_host')

        config = {
            'user': user,
            'password': password,
            'host': host,
            'database': 'baike',
            'raise_on_warnings': True
        }
        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor()

    def insert(self, value, sql):
        self.cursor.execute(sql, value)

        self.cnx.commit()
        self.cnx.close()

    def getLast(self, getlast_sql):
        self.cursor.execute(getlast_sql)
        result = self.cursor.fetchone()
        if result is not None:
            last_one = result[0]
        else:
            last_one = 0

        self.cnx.commit()
        self.cnx.close()

        return last_one


