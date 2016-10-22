# coding:utf8
from common import url_manage, html_download, html_parser, html_export, mysqldb

class SpiderMain(object):
    def __init__(self):
        # url manage
        self.urls = url_manage.UrlManager()
        # url download
        self.download = html_download.HtmlDownload()
        # url parser
        self.parser = html_parser.HtmlParser()
        # html export
        self.export = html_export.HtmlExport()
        #mysql
        self.msq = mysqldb.MysqlDB()

    def getUrl(self):
        url = 'https://movie.douban.com/j/search_subjects'
        self.craw(url)

    def craw(self, url):
        html_content = self.download.download(url)

        dom_element = self.parser.parse(html_content)

        #导演
        director = dom_element.find('a', rel="v:directedBy").text
        print director
if __name__ == "__main__":
    obj_spider = SpiderMain()
    obj_spider.getUrl()
