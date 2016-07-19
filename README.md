项目名称

=========

gooseeker

集搜客即时模式网络爬虫项目

项目背景
========
在python 即时网络爬虫项目启动说明中我们讨论一个数字：程序员浪费在调测内容提取规则上的时间。 网络数据抓取的工作量有80%是在为各种网站的各种数据结构编写抓取规则。

所以我们发起了这个项目，把程序员从繁琐的调测规则中解放出来，投入到更高端的数据处理工作中。

GooSeeker发布基于xslt的内容提取器，xslt可以通过GooSeeker API获得，让大家能省掉90%的调测正则表达式或者XPath的时间


项目资源
========
入口页

* http://www.gooseeker.com/land/python.html

Python交流园地

* http://www.gooseeker.com/doc/forum-59-1.html

知乎专栏

* https://zhuanlan.zhihu.com/gooseeker

GooSeeker收割模式网络爬虫

* http://www.gooseeker.com

项目目录文件说明
================
gooseeker

	- core/gooseeker.py 提取器类
	- core/README  说明文件

	- crawler/anjuke.py  采集安居客房产经纪人
	- crawler/result1.xml  安居客房产经纪人结果文件1
	- crawler/result2.xml  安居客房产经纪人结果文件2
	- crawler/crawl_gooseeker_bbs.py  采集集搜客论坛内容
	- crawler/xslt_bbs.xml  集搜客论坛内容提取本地xslt文件
	- crawler/douban.py  采集豆瓣小组讨论话题

	- crawler/simpleSpider  一个小爬虫(基于Scrapy开源框架)
	- crawler/tmSpider  采集天猫商品信息(基于Scrapy开源框架)

	- test/readPdf.py  python读取pdf文档