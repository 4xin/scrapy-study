# -*- coding: utf-8 -*-

# Scrapy settings for Downloader project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'CNSpider'

SPIDER_MODULES = ['CNSpider.spiders']
NEWSPIDER_MODULE = 'CNSpider.spiders'


RANDOMIZE_DOWNLOAD_DELAY = True
COOKIES_ENABLED = False
RETRY_ENABLED = False
DOWNLOAD_DELAY = 2

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True

DOWNLOADER_MIDDLEWARES = {  
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'CNSpider.rotate_useragent.RotateUserAgentMiddleware' :400
    }

SPIDER_MIDDLEWARES = {
    'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': 500,
}

REDIS_HOST = '192.168.1.132'
REDIS_PORT = 6379
