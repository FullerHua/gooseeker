# _*_coding:utf8_*_
# crawler_gooseeker_bbs.py
# 版本: V1.0

from urllib import request
from lxml import etree
from gooseeker import GsExtractor

# 访问并读取网页内容
url = "http://www.gooseeker.com/cn/forum/7"
conn = request.urlopen(url)
doc = etree.HTML(conn.read())

bbsExtra = GsExtractor()   
bbsExtra.setXsltFromAPI("98adf83ksdf0slrwaerwersdkfjsa" , "gooseeker_bbs_xslt")   # 设置xslt抓取规则，第一个参数是app key，请到会员中心申请
result = bbsExtra.extract(doc)   # 调用extract方法提取所需内容

print(str(result))

