# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
from twisted.enterprise import adbapi


class CrawlerPipeline(object):
    i = 0
    j = 0
    def __init__(self, dbpool):
        self.dbpool = dbpool


    @classmethod
    def from_settings(cls, settings):  # 函数名固定，会被scrapy调用，直接可用settings的值
        """
        数据库建立连接
        :param settings: 配置参数
        :return: 实例化参数
        """
        adbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            cursorclass=pymysql.cursors.DictCursor  # 指定cursor类型
        )

        # 连接数据池ConnectionPool，使用pymysql或者Mysqldb连接
        dbpool = adbapi.ConnectionPool('pymysql', **adbparams)
        # 返回实例化参数
        return cls(dbpool)

    def process_item(self, item, spider):
        """
        使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
        """
        query = self.dbpool.runInteraction(self.do_insert, ItemAdapter(item))  # 指定操作方法和操作数据
        print("\n\n\n\n-------------------分隔符 执行process_itemt第{0}次-------------------\n\n\n\n".format(self.j))
        self.j = self.j +1
        # 添加异常处理
        query.addCallback(self.handle_error)  # 处理异常

    def do_insert(self, cursor, item):
        # 对数据库进行插入操作，并不需要commit，twisted会自动commit
        insert_sql = """
        insert into mindmap_baidu(title, url, parentid, mid, root, nodetype, source, a, b, c, d, e) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(insert_sql, (item['title'], item['url'], item['parentid'], item['mid'], item['root'], item['nodetype'], item['source'], item['a'], item['b'], item['c'], item['d'], item['e'] ))
        print("\n\n\n\n-------------------分隔符 执行do_insert第{0}次-------------------\n\n\n\n".format(self.i))
        self.i = self.i + 1
    def handle_error(self, failure):
        if failure:
            # 打印错误信息
            print(failure)

