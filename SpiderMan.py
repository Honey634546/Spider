from DataOutput import DataOutput
from HTMLDownloader import HTMLDownloader
from HTMLParser import HTMLParser
from URLManager import URLManager

class SpiderMan(object):
    def __init__(self):
        self.manager=URLManager()
        self.downloader=HTMLDownloader()
        self.parser=HTMLParser()
        self.output=DataOutput()

    def crwal(self,root_url):
        # 添加入口url
        self.manager.add_new_url(root_url)
        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                new_url=self.manager.get_new_url()
                html=self.downloader.download(new_url)
                new_urls,data=self.parser.parser(new_url,html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print("已经抓取%s个连接"%self.manager.old_url_size())
            except Exception:
                print("crwal failed")
        self.output.oupput_html()

if __name__=="__main__":
    spider=SpiderMan()
    spider.crwal("https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB")
