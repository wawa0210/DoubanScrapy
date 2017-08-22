# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from douban.items import DbNovelItem

class DbnovelSpider(scrapy.Spider):
    name = 'dbnovel'
    allowed_domains = ['https://book.douban.com/']
    # start_urls = ['https://book.douban.com/tag/小说?start=0/']

    def start_requests(self):
        yield Request('https://book.douban.com/tag/',callback=self.parselink)

    # 爬取链接信息
    def parselink(self,response):
        selector = scrapy.Selector(response)

        # 提取链接信息包含的指向第二级的链接
        contenturllinks=selector.xpath('//table[@class="tagCol"]//td/a/@href').extract()
        for url in contenturllinks:

            yield Request('https://book.douban.com/'+url+'?start=0/',callback=self.parseitem,dont_filter=True)


        # 正式爬取内容
    def parseitem(self, response):

        selector=scrapy.Selector(response)
        novels=selector.xpath('//ul[@class="subject-list"]/li')
        for novel in novels:
            item = DbNovelItem()

            novelItemhtml=novel.xpath('div[@class="info"]')

            try:

                # 小说明细信息
                novelDetail=novelItemhtml.xpath('div[@class="pub"]/text()').extract()[0].replace('\n','').replace(' ','').split('/')[::-1]
                item['name']=novelItemhtml.xpath('h2//a/text()').extract()[0].replace(' ','').replace('\n','')
                item['star']=novelItemhtml.xpath('div[@class="star clearfix"]/span[@class="rating_nums"]/text()').extract()[0]
                item['commentNum']=novelItemhtml.xpath('div[@class="star clearfix"]/span[@class="pl"]/text()').extract()[0].replace('\n','').replace(' ','').replace('人评价)','').replace('(','')

                des=novelItemhtml.xpath('p/text()').extract()

                try:
                    if des is not None:
                        item['deccrption']=novelItemhtml.xpath('p/text()').extract()[0]

                except Exception as err:
                    print(err)

                try:
                    if des is not None:
                        item['publishcompany'] = novelDetail[2]
                except Exception as err:
                    print(err)

                try:
                    if des is not None:
                        item['publishdate'] = novelDetail[1]
                except Exception as err:
                    print(err)

                try:
                    if des is not None:
                        item['price'] = novelDetail[0]
                except Exception as err:
                    print(err)

                try:
                    if des is not None:
                        item['author'] = str(novelDetail[3:])
                except Exception as err:
                    print(err)

                yield item
            except Exception as err:
                print(err)


        # 获得下一页链接 继续爬取

        nexturl=selector.xpath('//div[@class="paginator"]/span[@class="thispage"]/following-sibling::a[1]/@href').extract()

        if nexturl is not None and nexturl!='':
            yield Request('https://book.douban.com'+nexturl[0],meta={'item':item},callback=self.parseitem,dont_filter=True)
