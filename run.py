import os

from scrapy import cmdline


# cmdline.execute('scrapy crawl baidu_spider -a keyword=https://www.baidu.com/s?ie=UTF-8&wd=bilibili'.split())
# cmdline.execute(['scrapy', 'crawl', 'baidu_spider', "-a", "keyword=scrapy"])


# 要同时执行，否则执行的每一条命令是作用在当前目录下，
# 所以要cd转跳的瞬间（os.system前半句还未执行完的瞬间）
# 把python run.py执行完
# 教训： 因为用的是cmd命令来传递参数，所以字符串不可以有空格，多一个空格就会改变后面命令的意思

keyword = '目的'
parentid = '人工智能'
root = '人工智能'

cmd = 'cd C:/chenjimiao/project/python/aiTeacherPlan/project/crawler/ && scrapy crawl baidu_spider -a keyword=' + keyword + ' -a parentid=' + parentid + ' -a root=' + root

test = os.system(cmd)
