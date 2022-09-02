from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class someSpider(CrawlSpider):
    name = "geturl"
    item = []

    allowed_domains = ["aclanthology.org"]
    start_urls = ["https://aclanthology.org/"]

    rules = (Rule(LinkExtractor(), callback="parse_obj", follow=True),)

    def parse_obj(self, response):
        filename = "links.txt"
        with open(filename, "a") as f:
            f.write(str(response.url) + "\n")
        self.log("Saved file %s" % filename)
