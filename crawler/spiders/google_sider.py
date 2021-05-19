import scrapy


class GoogleSiderSpider(scrapy.Spider):
    name = 'google_sider'
    allowed_domains = ['google.com']
    start_urls = ['http://google.com/']

    def parse(self, response):
        pass
