# -*- coding: utf-8 -*-
import scrapy
import sys
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from mvsgst.items import MvsgstItem
from scrapy.selector import HtmlXPathSelector
import time
import re
import random

class DbmvSpider(scrapy.Spider):
    name = "vcmv"
    tags = []
#    for i in range(1900,2016,1):
#        tags.append( "http://movie.douban.com/tag/"+str(i))
    start_urls = ("http://www.verycd.com/base/movie/~all/",) #tuple(tags)

    def load_item(self,ct):
        staticurl = "http://www.verycd.com"
        item = MvsgstItem()
        item['url']=[]
        for i in ct.xpath('@href').extract():
                item['url'].append(staticurl+i)
        return item

    def regprocess(self,lst):
        ret  = []
        for i in lst:
            i=i.replace('"','')
            i=i.replace(',','')
            i=i.replace(u'\u201c',u'')
            ret.append(i)
        return ret
 

    def load_detail(self,itemurl):
        dre = re.compile(ur'\u4e0a\u6620\u65e5\u671f.*\>(.*)\<\/em\>')
        details = itemurl.meta['item']         
        x = scrapy.Selector(itemurl)
        details['mvname']= x.xpath('//*[@class="titleDiv"]/h1/text()').extract()
        enn = x.xpath('//*[@class="titleDiv"]/h2/text()').extract()
        details['enname'] = self.regprocess(enn)
        
        details['director']=x.xpath('//*[@rel="v:directedBy"]/text()').extract()
        details['actors']=x.xpath('//*[@rel="v:starring"]/text()').extract()
        details['types']=x.xpath('//*[@rel="v:genre"]/text()').extract()
        details['date'] = dre.findall(itemurl.body.decode('utf8'))
        details['length'] = x.xpath('//*[@property="v:runtime"]/text()').extract()
        summ= x.xpath('//*[@property="v:summary"]/p/text()').extract()
        details['summary'] = self.regprocess(summ)
        
        #details['rank']= x.xpath('//*[@id="scoreDivDiv"]/text()').extract()
        #TODO this place should be rebuilt, but for this case, enough
        time.sleep(random.randint(1,3))
        return details

    def parse(self, response):

        x = scrapy.Selector(response)
        sites = x.xpath('//*[@class="clearfix entry_cover_list"]/li/a')
        i=0
        for ct in sites:
            i+=1
            item = self.load_item(ct)
            yield scrapy.Request(item['url'][0],meta={'item':item},callback=self.load_detail)
        time.sleep(random.randint(3,10))
        nexturl=x.xpath('//*[@rel="next"]/@href').extract()
        if len(nexturl)>0:
            yield scrapy.Request('http://www.verycd.com'+nexturl[0],callback=self.parse)  
        #if i==10:
        #    sys.exit(0)
