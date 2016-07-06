# _*_coding:utf8_*_
# anjuke.py
# 爬取安居客房产经纪人

from urllib import request
from lxml import etree
from gooseeker import GsExtractor

totalpages = 50

class Spider:
    def getContent(self, url):
        conn = request.urlopen(url)
        output = etree.HTML(conn.read())
        return output

    def saveContent(self, filepath, content):
        file_obj = open(filepath, 'w', encoding='UTF-8')
        file_obj.write(content)
        file_obj.close()

bbsExtra = GsExtractor()   
bbsExtra.setXsltFromAPI("31d24931e043e2d5364d03b8ff9cc77e" , "安居客房产经纪人")   # 设置xslt抓取规则，第一个参数是app key，请到会员中心申请

url = "http://shenzhen.anjuke.com/tycoon/nanshan/p"
anjukeSpider = Spider()
print("爬取开始")

for pagenumber in range(1 , totalpages):
    currenturl = url + str(pagenumber)
    print("正在爬取", currenturl)
    content = anjukeSpider.getContent(currenturl)
    outputxml = bbsExtra.extract(content)
    outputfile = "result" + str(pagenumber) + ".xml"
    anjukeSpider.saveContent(outputfile , str(outputxml))

print("爬取结束")


