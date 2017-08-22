# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):

    # 书名
    bookname=scrapy.Field()
    # 作者
    author=scrapy.Field()
    # 出版社
    publishcompany=scrapy.Field()
    # 出版时间
    publishdate=scrapy.Field()
    # 价格
    price=scrapy.Field()

    # 星级
    star=scrapy.Field()

    # 评价数量
    ratenums=scrapy.Field()

    # 简要描述
    descrption=scrapy.Field()

class JianshuItem(scrapy.Item):
    title=scrapy.Field()
    author=scrapy.Field()
    url=scrapy.Field()
    readNum=scrapy.Field()
    commentNum=scrapy.Field()
    likeNum=scrapy.Field()
    deccrption=scrapy.Field()


# 豆瓣小说
class DbNovelItem(scrapy.Item):
    name=scrapy.Field()
    star=scrapy.Field()
    commentNum=scrapy.Field()
    deccrption=scrapy.Field()
    # 出版社
    publishcompany = scrapy.Field()
    # 出版时间
    publishdate = scrapy.Field()
    # 价格
    price = scrapy.Field()

    # 作者
    author = scrapy.Field()