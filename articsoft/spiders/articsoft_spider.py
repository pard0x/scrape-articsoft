# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from articsoft.items import ArticsoftItem
from html2text import HTML2Text

class ArticsoftSpider(CrawlSpider):
	name = "articsoft"
	allowed_domains = ["articsoft.com"]
	start_urls = ["http://www.articsoft.com/information_security.htm"]

	def parse(self, response):
		for box in response.xpath('//ul'):
			for root in box.xpath('.//li'):
				link = root.css('a[href*=htm]::attr(href)').extract()
				if link[0]:
					yield Request("http://www.articsoft.com/"+link[0],
								  callback=self.parse_text)
		
	def parse_text(self, response):
		# parse text and save to file
		converter = HTML2Text()
		root = response.css('td[id*=content]')
		item = ArticsoftItem()
		item["name"] = root.xpath('.//h1/text()').extract()
		item["href"] = response.url
		item["category"] = "tech"
		item["text"] = converter.handle(root.extract()[0])
		return item

	# def start_requests(self):
	# 	return [FormRequest("http://www.example.com/login",
	# 			formdata={"user":"user", "pass":"pass", },
	# 			callback=self.logged_in)]

	# def logged_in(self):
	# 	# extract links to follow and return Requests for each of them, with another callback