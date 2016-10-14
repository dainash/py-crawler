import mysqldb


class HtmlExport(object):
    def __init__(self):
        pass

    def collect_data(self, data):
        msq = mysqldb.MysqlDB()
        msq.insert(data)

    def output_html(self):
        pass
