import requests


class HtmlDownload(object):
    def download(self, url):
        if url is None:
            return None
        try:
            result = requests.get(url, timeout=3)
            if result.status_code != 200:
                return None
            result.encoding = "utf-8"
            text = result.text
            return text
        except requests.RequestException, e:
            return e