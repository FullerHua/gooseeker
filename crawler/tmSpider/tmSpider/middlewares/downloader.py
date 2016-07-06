# -*- coding: utf-8 -*-
import time
from scrapy.exceptions import IgnoreRequest
from scrapy.http import HtmlResponse, Response
from selenium import webdriver
import selenium.webdriver.support.ui as ui 

class CustomDownloader(object):
    def __init__(self):
        # use any browser you wish
        cap = webdriver.DesiredCapabilities.PHANTOMJS
        cap["phantomjs.page.settings.resourceTimeout"] = 1000
        cap["phantomjs.page.settings.loadImages"] = True
        cap["phantomjs.page.settings.disk-cache"] = True
        cap["phantomjs.page.customHeaders.Cookie"] = 'SINAGLOBAL=3955422793326.2764.1451802953297; '
        self.driver = webdriver.PhantomJS(executable_path='F:/phantomjs/bin/phantomjs.exe', desired_capabilities=cap)
        #wait = ui.WebDriverWait(self.driver,10)
    
    def VisitPersonPage(self, url):
        print('正在加载网站.....')
        self.driver.get(url)
        time.sleep(1)
        # 翻到底，详情加载
        js="var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(5)
        content = self.driver.page_source.encode('gbk','ignore')
        print('网页加载完毕.....')
        return content

    def __del__(self):
        self.driver.quit()