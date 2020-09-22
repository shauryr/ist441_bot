
from scrapy.selector import Selector

from scrapy.linkextractors import LinkExtractor
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request


URL = 'https://www.aclweb.org/anthology/'


class FollowAllSpider(CrawlSpider):
	name = 'ist441_bot'
	start_urls = ['https://www.aclweb.org/anthology/']
	rules = [Rule(LinkExtractor(),callback='parse_item',follow=True)]
	allowed_domains = ['www.aclweb.org/anthology/']
	def parse_items(self, response):
		hxs = Selector(response)
		for url in hxs.select('//a/@href').extract():
			if not (url.startswith('https://') or url.startswith('https://')):
				url = URL + url
				print(url)
			yield Request(url, callback=self.parse)
