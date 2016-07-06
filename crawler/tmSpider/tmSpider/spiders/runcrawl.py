# -*- coding: utf-8 -*-

import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner

from tmall import TmallSpider

spider = TmallSpider(domain='tmall.com')
crawler = CrawlerRunner()
crawler.crawl(spider)
d = crawler.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()
