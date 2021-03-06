# -*- coding: utf-8 -*-
import scrapy
import sys
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from mvsgst.items import MvsgstItem
from scrapy.selector import HtmlXPathSelector
import time
import re

class DbmvSpider(scrapy.Spider):
    name = "dbmv"
    tags = []
    for i in range(1900,2016,1):
        tags.append( "http://movie.douban.com/tag/"+str(i))
    start_urls = ("http://movie.douban.com/tag/1901/",) #tuple(tags)

    def load_item(self,ct):
        item = MvsgstItem()
        item['url']=ct.xpath('@href').extract()
        return item

    def load_detail(self,itemurl):
        pre1 =re.compile(ur'\/\u5730\u533a\:.*br\/>')
        pre2 = re.compile(ur'\u8bed\u8a00\:.*\<b')
        pre3 = re.compile(ur'\>(.*)\<')
 
        details = itemurl.meta['item']         
        x = scrapy.Selector(itemurl)
        details['mvname']= x.xpath('//*[@property="v:itemreviewed"]/text()').extract()
        details['director']=x.xpath('//*[@rel="v:directedBy"]/text()').extract()
        details['actors']=x.xpath('//*[@rel="v:starring"]/text()').extract()
        details['types']=x.xpath('//*[@property="v:genre"]/text()').extract()
        details['date'] = x.xpath('//*[@property="v:initialReleaseDate"]/text()').extract()
        details['length'] = x.xpath('//*[@property="v:runtime"]/text()').extract()
        details['summary'] = x.xpath('//*[@property="v:summary"]/text()').extract()
        #TODO this place should be rebuilt, but for this case, enough
        type(itemurl.body)
        details['areas'] = pre3.findall(pre1.findall(itemurl.body.decode('utf8')))
        details['language']=pre3.findall(pre2.findall(itemurl.body.decode('utf8')))
        return details

    def parse(self, response):

        x = scrapy.Selector(response)
        sites = x.xpath('//*[@id="content"]/div/div/div/table/tr/td/a')
        for ct in sites:
            item = self.load_item(ct)
            yield scrapy.Request(item['url'][0],meta={'item':item},callback=self.load_detail)

        nexturl=x.xpath('//*[@class="next"]/a/@href').extract()
        if len(nexturl)!=0:
            print str(nexturl[0])
            yield scrapy.Request(nexturl[0],callback=self.parse)  
