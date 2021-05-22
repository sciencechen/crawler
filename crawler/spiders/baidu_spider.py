import scrapy
import uuid

# 疑惑：为什么加..就可以了
from ..items import CrawlerItem


class BaiduSpiderSpider(scrapy.Spider):
    name = 'baidu_spider'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?ie=UTF-8&wd=baidu']
    parentid = ''
    root = ''

    def __init__(self, keyword=None, parentid=None, root=None, *args, **kwargs):
        super(BaiduSpiderSpider, self).__init__(*args, **kwargs)
        # 因为start_urls是列表，所以用这种方法把传入的字符串变成列表
        url = 'https://www.baidu.com/s?ie=UTF-8&wd=' + keyword
        self.parentid = parentid
        self.root = root


        self.start_urls = url.split(' ')
        print('start_urls为：', self.start_urls)

    def parse(self, response):

        titles = response.xpath("/html/body//div[2]/div/@data-tools").re("""[:]["].*["][,]""")
        urls = response.xpath("/html/body//div[2]/div/@data-tools").re('''["][h][t][t].*["][}]''')
        print("\n\n\n\n-------------------分隔符-------------------\n\n\n\n")
        print(titles)
        print("titles的长度是： ", len(titles))
        print("\n\n\n\n-------------------分隔符-------------------\n\n\n\n")
        print(urls)
        print("urls的长度： ", len(urls))
        print("\n\n\n\n-------------------分隔符-------------------\n\n\n\n")
        i = 0
        for title in titles:
            item = CrawlerItem()
            print({
                # replace ：去除正则时匹配到的多余的字符
                "titles": title.replace(':', '').replace('"', '', 2).replace(',', ''),
                'url': urls[i].replace('"', '').replace('}', '')
            })
            item['url'] = urls[i].replace('"', '').replace('}', '')
            item['title'] = title.replace(':', '').replace('"', '', 2).replace(',', ''),
            # 暂时为root
            item['parentid'] = self.parentid
            item['mid'] = uuid.uuid1()
            item['root'] = self.root
            # 因为目前爬出来的都是URL，所以统一爬出来的结果为a
            item['nodetype'] = 'a'

            item['source'] = 'baidu'
            item['a'] = 'xx'
            item['b'] = 'xx'
            item['c'] = 'xx'
            item['d'] = 'xx'
            item['e'] = 'xx'





            yield item
            print("\n\n\n\n-------------------分隔符 执行yield item第{0}次-------------------\n\n\n\n".format(i))
            i = i + 1


        pass
