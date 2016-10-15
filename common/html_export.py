import mysqldb


class HtmlExport(object):
    def __init__(self):
        pass

    def collect_data(self, data, sql):
        msq = mysqldb.MysqlDB()
        msq.insert(data, sql)

    def output_html(self):
        pass
