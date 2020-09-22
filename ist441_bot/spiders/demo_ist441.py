from scrapy import Spider
from scrapy.linkextractors import LinkExtractor

class MySpider(Spider):
    name = 'jupider'
    start_urls = ['https://acl-arc.comp.nus.edu.sg/archives/acl-arc-160301-pdf/']

    def parse(self, response):
        le = LinkExtractor()
        for link in le.extract_links(response):
            print(link.url)
