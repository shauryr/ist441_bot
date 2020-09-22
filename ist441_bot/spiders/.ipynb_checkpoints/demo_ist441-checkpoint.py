from scrapy import Spider
from scrapy.linkextractors import LinkExtractor

class MySpider(Spider):
    name = 'jupider'
    start_urls = ['https://www.cs.rit.edu/~dprl/mathseer/']

    def parse(self, response):
        le = LinkExtractor()
        for link in le.extract_links(response):
            print(link.url)
