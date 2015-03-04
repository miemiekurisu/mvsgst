# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MvsgstItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    mvname = scrapy.Field()
    dirctor = scrapy.Field()
    actors = scrapy.Field()
    types = scrapy.Field()
    areas = scrapy.Field()
    lang = scrapy.Field()
    date = scrapy.Field()
    length = scrapy.Field()
    imdblink = scrapy.Field()
    outline = scrapy.Field()
    pass
