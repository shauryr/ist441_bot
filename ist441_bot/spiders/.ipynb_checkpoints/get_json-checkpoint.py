import scrapy
import json

class JsonSpider(scrapy.Spider):
    name = 'urlgetjson'
    def __init__(self, filename=None):
#          read urls from files
        if filename:
            with open(filename,'r') as f:
                self.start_urls = [url.strip() for url in f.readlines()]
    def parse(self, response):
#         get only text from html reponse
        all_text = ''.join(response.selector.select('//body//text()').extract()).strip().replace('\r\n', '')
        title_text = ''.join(response.selector.select('//title//text()').extract()).strip()
        yield {'url' : response.url, 'body': all_text, 'title': title_text ,'status' : response.status}
        