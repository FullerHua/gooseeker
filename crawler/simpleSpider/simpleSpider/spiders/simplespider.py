# -*- coding: utf-8 -*-
import time
import scrapy
from lxml import etree
from selenium import webdriver
import gooseeker.GsExtractor as GsExtractor

class SimpleSpider(scrapy.Spider):
    name = "simplespider"
    allowed_domains = ["taobao.com"]
    start_urls = [
        "https://item.taobao.com/item.htm?spm=a230r.1.14.197.e2vSMY&id=44543058134&ns=1&abbucket=10"
    ]

    def __init__(self):
        # use any browser you wish
        self.browser = webdriver.Firefox()
    
    # 获得当前时间戳
    def getTime(self):
        current_time = str(time.time())
        m = current_time.find('.')
        current_time = current_time[0:m]
        return current_time
       
    def parse(self, response):
        print("start...")
        #start browser
        self.browser.get(response.url)
        #loading time interval
        time.sleep(3)
        #get xslt
        extra=GsExtractor()
        extra.setXsltFromAPI("0a3898683f265e7b28991e0615228baa", "淘宝天猫_商品详情30474")
        # get doc
        html = self.browser.execute_script("return document.documentElement.outerHTML")
        doc = etree.HTML(html)
        result = extra.extract(doc)
        
        # out file
        file_name = 'F:/temp/淘宝天猫_商品详情30474_' + self.getTime() + '.xml'
        open(file_name,"wb").write(result)
        self.browser.close()
        print("end")
       
        
