# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ArticsoftPipeline(object):
    def process_item(self, item, spider):
        return item

# class ArticsoftSQLitePipeline(object):
# 	def __init__(self):
# 		import sqlite3 as lite
# 		import os
# 		import sys

# 		con = lite.connect('articsoft.db')

# 		with con:
			
