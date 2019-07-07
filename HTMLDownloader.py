import requests

class HTMLDownloader(object):
    def download(self,url):
        if url is None:
            return None
        headers={
            'user-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        res=requests.get(url,headers=headers)
        if res.status_code==200:
            res.encoding='utf-8'
            return res.text
        return None


if __name__=="__main__":
    load=HTMLDownloader()
    print(load.download("http://www.baidu.com"))

        