from scrapy import cmdline


# cmdline.execute('scrapy crawl baidu_spider -a keyword=https://www.baidu.com/s?ie=UTF-8&wd=bilibili'.split())
cmdline.execute(['scrapy', 'crawl', 'baidu_spider', "-a", "keyword=scrapy"])