# -*- coding: utf-8 -*-
import scrapy
from BBSSpider.items import BbsspiderItem

class Cn5SpiderSpider(scrapy.Spider):
    name = "CN5Spider"
    allowed_domains = ["cangnan5.com"]
    start_urls = (
        'http://www.cangnan5.com/forum-143-1.html',
    )

    def parse(self, response):
        records = response.xpath('//tbody[re:test(@id, "normalthread_\d+")]/tr/th/a[3]')
        for record in records:
            item = BbsspiderItem()
            item['url'] = record.xpath('@href').extract()
            item['title'] = record.xpath('text()').extract()
            yield  item
