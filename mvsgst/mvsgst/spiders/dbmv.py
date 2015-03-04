# -*- coding: utf-8 -*-
import scrapy
import sys
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from mvsgst.items import MvsgstItem
from scrapy.selector import HtmlXPathSelector
import time

class DbmvSpider(scrapy.Spider):
    name = "dbmv"
    tags = []
    for i in range(1900,2016,1):
        tags.append( "http://movie.douban.com/tag/"+str(i))
    start_urls = tuple(tags)

    def load_item(self,ct):
        item = MvsgstItem()
        item['url']=ct.xpath('@href').extract()
        return item

    def parse(self, response):
        x = scrapy.Selector(response)
        sites = x.xpath('//*[@id="content"]/div/div/div/table/tr/td/a')
        for ct in sites:
            item = self.load_item(ct)
            print item['url']
