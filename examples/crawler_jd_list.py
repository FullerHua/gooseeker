# -*- coding:utf-8 -*- 
# 爬取京东商品列表， 以手机商品列表为例
# 示例网址：http://list.jd.com/list.html?cat=9987,653,655&page=1&JL=6_0_0&ms=5
# crawler_jd_list.py
# 版本: V1.0

from urllib import request
from lxml import etree
from selenium import webdriver
from gooseeker import gsExtractor
import time

class Spider:
    def __init__(self):
        self.scrollpages = 0
        self.waittime = 3
        self.phantomjsPath = 'C:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'

    def getContent(self, url):
        browser = webdriver.PhantomJS( executable_path = self.phantomjsPath )
        browser.get(url)
        time.sleep(self.waittime)
        html = browser.execute_script("return document.documentElement.outerHTML")
        doc = etree.HTML(html)
        jdlistExtra = gsExtractor()
        jdlistExtra.setXsltFromFile("jd_list.xml")
        output = jdlistExtra.extract(doc)
        return output

    def saveContent(self, filepath, content):
        file_obj = open(filepath,'w',encoding='UTF-8')
        file_obj.write(content)
        file_obj.close()

url = 'http://list.jd.com/list.html?cat=9987,653,655&page=1&JL=6_0_0&ms=5'
jdspider = Spider()
result = jdspider.getContent(url)
jdspider.saveContent('京东手机列表_1.xml',str(result))

