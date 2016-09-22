from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, html_content):
        try:
            soup = BeautifulSoup(html_content, "html.parser")
        except:
            soup = False
        return soup