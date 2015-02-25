# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DichanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    area = scrapy.Field()
    section = scrapy.Field()
    type = scrapy.Field()
    floor = scrapy.Field()
    roomtype = scrapy.Field()
    decorate = scrapy.Field()
    acreage = scrapy.Field()
    unit_price = scrapy.Field()
    price = scrapy.Field()
    date = scrapy.Field()
    pass
