#!/usr/bin/python
# -*- coding: utf-8 -*-
# 模块名: gooseeker
# 类名: gsExtractor
# Version: 1.0
# 说明: html内容提取器
# 功能: 使用xslt作为模板，快速提取HTML DOM中的内容。
# released by 集搜客(http://www.gooseeker.com) on May 18, 2016
# github: https://github.com/FullerHua/jisou/core/gooseeker.py

from urllib import request
from lxml import etree
import time

class xsltExtractor(object):
    xslt = ""
    def _init_(self):
        xslt = ""
    # 从文件读取xslt
    def setXsltFromFile(self , xsltFilePath):
        file = open(xsltFilePath , 'r' , encoding='UTF-8')
        try:
            self.xslt = file.read()
        finally:
            file.close()
    # 从字符串获得xslt
    def setXsltFromMem(self , xsltStr):
        self.xslt = xsltStr
    # 预留:通过API接口获得xslt
    def setXsltFromAPI(self):
        self.xslt = ""
    # 返回当前xslt
    def getXslt(self):
        return self.xslt
    # 提取方法，入参是一个HTML DOM对象，返回是提取结果
    def extract(self , html):
        xslt_root = etree.XML(self.xslt)
        transform = etree.XSLT(xslt_root)
        result_tree = transform(html)
        return result_tree