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

    def craw(self):
        getlast_sql = 'select `index` from page_data order by id DESC limit 1'
        i = self.msq.getLast(getlast_sql)
        while True:
            root_url = "http://baike.baidu.com/view/" + str(i+1) + ".htm"
            # 获取源代码
            html_content = self.download.download(root_url)

            err_page = "errorBox" in html_content

            if not err_page:
                # 转换dom
                dom_element = self.parser.parse(html_content)

                if dom_element:

                    # 获取标题,描述,图片
                    title = dom_element.select('.lemmaWgt-lemmaTitle-title h1')[0].text
                    try:
                        desc = dom_element.select('.lemma-summary')[0].text
                    except:
                        desc = ''
                    try:
                        img = dom_element.select('.summary-pic img')[0]['src']
                    except:
                        img = ''

                    dict = (title, img, desc, i)
                    insert_sql = ("INSERT INTO page_data "
                   "(title, img, description, `index`) "
                   "VALUES (%s, %s, %s, %s)")
                    # 存储数据
                    if title and desc:
                        self.export.collect_data(dict, insert_sql)
                        print 'crawed ' + str(i) + ' success'
                    else:
                        print 'crawed data' + str(i) + 'empty desc'
                else:
                    print 'crawed ' + str(i) + ' parse failed'
                i += 1
            else:
                i += 1
                print 'crawed ' + str(i) + ' err_page failed'


if __name__ == "__main__":
    obj_spider = SpiderMain()
    obj_spider.craw()
