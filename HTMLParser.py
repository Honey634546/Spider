import re
import urllib.parse
from bs4 import BeautifulSoup

# 名词解释： 不超过二十字数
# 互斥
# 填空
# 页面置换算法
# 计算虚拟页面大小
# 简答
# 
# 原理及方法

# 第一章
# 掌握操作系统的基本概念
# 了解操作系统的发展历史及各阶段的主要特征
# 掌握操作系统的组成(简答题)
# 掌握操作系统的类型(简答题) 实时系统...
# 掌握系统调用,多道程序感念(不到十个字)
# 了解操作系统发展中的各种典型结构
# p33 掌握操作系统的分层结构  图

# 第二张
# 竞争条件、临界区、临界资源、原语操作、进程互斥、进程同步、进程控制块、、、进程调度
# 生产者消费者问题
# 程序是静态的，进程是动态的
# 程序是永久的、进程是暂时的
# 进程状态转换！！！！！！！图记住


# P\V操作解决互斥问题、同步问题

# 共享设备
# 独占设备
# 块设备
# 字符设备




class HTMLParser(object):
    def parser(self,page_url,html_cont):
        """
        用于解析网页内容，抽取URL和数据
        :param page_url: 下载页面的url
        :param html_cont: 下载的网页内容
        :return:返回url和数据
        """
        if page_url is None or html_cont is None:
            return 
        soup=BeautifulSoup(html_cont,'html.parser')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self,page_url,soup):
        """
        抽取新的url集合
        :param page_url:下载页面的url
        :param soup:soup
        :return:返回新的url集合
        """
        new_urls=set()
        links=soup.findAll('a',href=re.compile(r'/item/.*/\d+'))
        # print(links)
        for link in links:
            new_url=link['href']
            new_full_url=urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        """
        抽取有效数据
        :param page_url:下载页面的url
        :param soup:soup
        :return:返回有效数据
        """
        data={}
        data['url']=page_url
        title=soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title']=title.get_text()
        summary=soup.find('div',class_='lemma-summary')
        data['summary']=summary.get_text()
        return data


if __name__=="__main__":
    parser=HTMLParser()
    parser.parser("https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB")