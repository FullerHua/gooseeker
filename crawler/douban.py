# _*_coding:utf8_*_
# douban.py
# 爬取豆瓣小组讨论话题

from urllib import request
from lxml import etree
from gooseeker import GsExtractor
from selenium import webdriver

class PhantomSpider:
    def getContent(self, url):
        browser = webdriver.PhantomJS(executable_path='C:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
        browser.get(url)
        time.sleep(3)
        html = browser.execute_script("return document.documentElement.outerHTML")
        output = etree.HTML(html)
        return output

    def saveContent(self, filepath, content):
        file_obj = open(filepath, 'w', encoding='UTF-8')
        file_obj.write(content)
        file_obj.close()

doubanExtra = GsExtractor()   
# 下面这句调用gooseeker的api来设置xslt抓取规则
# 第一个参数是app key，请到GooSeeker会员中心申请
# 第二个参数是规则名，是通过GooSeeker的图形化工具: 谋数台MS 来生成的
doubanExtra.setXsltFromAPI("ffd5273e213036d812ea298922e2627b" , "豆瓣小组讨论话题")  

url = "https://www.douban.com/group/haixiuzu/discussion?start="
totalpages = 5
doubanSpider = PhantomSpider()
print("爬取开始")

for pagenumber in range(1 , totalpages):
    currenturl = url + str((pagenumber-1)*25)
    print("正在爬取", currenturl)
    content = doubanSpider.getContent(currenturl)
    outputxml = doubanExtra.extract(content)
    outputfile = "result" + str(pagenumber) +".xml"
    doubanSpider.saveContent(outputfile , str(outputxml))

print("爬取结束")
