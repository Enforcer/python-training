import scrapy


class BlogSpider(scrapy.Spider):
    name = "blog"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
