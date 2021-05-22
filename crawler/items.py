# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    parentid = scrapy.Field()
    mid = scrapy.Field()
    root = scrapy.Field()
    nodetype = scrapy.Field()
    source = scrapy.Field()
    a = scrapy.Field()
    b = scrapy.Field()
    c = scrapy.Field()
    d = scrapy.Field()
    e = scrapy.Field()

    pass
