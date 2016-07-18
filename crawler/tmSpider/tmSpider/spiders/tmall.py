# -*- coding: utf-8 -*-
import time
import scrapy

import tmSpider.gooseeker.Gsextractor as gsextractor

class TmallSpider(scrapy.Spider):
    name = "tmall"
    allowed_domains = ["tmall.com"]
    start_urls = (
        'https://world.tmall.com/item/526449276263.htm',
    )
    
    # 获得当前时间戳
    def getTime(self):
        current_time = str(time.time())
        m = current_time.find('.')
        current_time = current_time[0:m]
        return current_time

    def parse(self, response):
        html = response.body
        print("----------------------------------------------------------------------------")
        extra=gsextractor.GsExtractor()
        extra.setXsltFromAPI("31d24931e043e2d5364d03b8ff9cc77e", "淘宝天猫_商品详情30474","tmall","list")

        result = extra.extract(html)
        print(str(result).encode('gbk','ignore').decode('gbk'))
        #file_name = 'F:/temp/淘宝天猫_商品详情30474_' + self.getTime() + '.xml'
        #open(file_name,"wb").write(result)