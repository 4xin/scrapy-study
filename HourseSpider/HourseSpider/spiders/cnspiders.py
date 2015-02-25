# -*- coding: utf-8 -*-
import scrapy
from HourseSpider.items import DichanItem

class HourseSpider(scrapy.Spider):
    name = "HourseSpider"
    allowed_domains = ["cnfce.net"]

    def __init__(self, category=None, *args, **kwargs):
        super(HourseSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.cnfce.net/sale/page1.html']

    def parse(self, response):
        data = response.xpath('//div[@id="mainn"]/ul[re:test(@class,"ul[0-1]$")]')
        for sel in data:
            item = DichanItem()
            item['area']= sel.xpath('li[re:test(@class,"lifw[0-1]$")]/a/text()').extract()
            item['section']= sel.xpath('li[re:test(@class,"lidd[0-1]$")]/a/text()').extract()
            item['type']= sel.xpath('li[re:test(@class,"lifx[0-1]$")]/a/text()').extract()
            item['floor']= sel.xpath('li[re:test(@class,"lilc[0-1]$")]/a/text()').extract()
            item['roomtype']= sel.xpath('li[re:test(@class,"lihx[0-1]$")]/a/text()').extract()
            item['decorate']= sel.xpath('li[re:test(@class,"lizx[0-1]$")]/a/text()').extract()
            item['acreage']= sel.xpath('li[re:test(@class,"limj[0-1]$")]/a/text()').extract()
            item['unit_price']= sel.xpath('li[re:test(@class,"lidj[0-1]$")]/a/text()').extract()
            item['price']= sel.xpath('li[re:test(@class,"lijg[0-1]$")]/a/text()').extract()
            item['date']= sel.xpath('li[re:test(@class,"lirq[0-1]$")]/a/text()').extract()
            yield item
