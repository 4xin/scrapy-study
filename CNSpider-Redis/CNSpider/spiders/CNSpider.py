# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor

def saveHtml(response):
    print response.url
    #处理页面内容代码

class CNSpider(CrawlSpider):
    name = "CNSpider"
    allowed_domains = []
    start_urls = []
    def __init__(self, *a, **kw):
        super(CNSpider, self).__init__(*a, **kw)
        for url in open("url.txt"):
            self.start_urls.append(url.strip())
        for domain in open("domains.txt"):
            self.allowed_domains.append(domain.strip())
    regex_cncn = '.*cncn.gov.cn/art/.*html'
    rules = [
            Rule(LinkExtractor(allow=[regex_cncn]), 'parse_cncn'),
            ]

    def parse_cncn(self,response):
        saveHtml(response)