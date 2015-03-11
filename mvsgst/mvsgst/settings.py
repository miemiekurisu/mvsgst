# -*- coding: utf-8 -*-

# Scrapy settings for mvsgst project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mvsgst'

SPIDER_MODULES = ['mvsgst.spiders']
NEWSPIDER_MODULE = 'mvsgst.spiders'

ITEM_PIPELINES = {'mvsgst.pipelines.MvsgstPipeline':800}

EXTENSIONS = {'scrapy.contrib.throttle.AutoThrottle':500,}

DOWNLOAD_DELAY = 2

#LOG_LEVEL = 'WARNING' 
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mvsgst (+http://www.yourdomain.com)'
