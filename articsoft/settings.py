# -*- coding: utf-8 -*-

# Scrapy settings for articsoft project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'articsoft'

SPIDER_MODULES = ['articsoft.spiders']
NEWSPIDER_MODULE = 'articsoft.spiders'

ITEM_PIPELINES = ['articsoft.pipelines.ArticsoftPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'articsoft (+http://www.yourdomain.com)'
