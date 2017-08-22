# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.http import Request
from douban.items import DoubanItem

# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor

class DbooksSpider(scrapy.Spider):
    name = 'dbooks'
    allowed_domains = ['http://www.douban.com']
    start_urls = ['https://book.douban.com/top250?start=0']
    # rules = {
    #     Rule(LinkExtractor(allow=(r'https://book.douban.com/top250?start=[0-9]+?')),callback='parse_item')
    # }

    def parse(self, response):
        htmlResponse=Selector(response);


        print(response.url)
        for bookitem in htmlResponse.xpath('//div[@class="indent"]/table'):
            item = DoubanItem()
            item['bookname'] = bookitem.xpath('//div[@class="pl2"]/a/text()').extract()[0].replace('\n','').replace(' ','')
            item['author'] = bookitem.xpath('//p[@class="pl"]/text()').extract()[0]
            item['star'] = bookitem.xpath('//span[@class="rating_nums"]/text()').extract()[0].replace('\n','').replace(' ','')
            item['ratenums'] = bookitem.xpath('//span[@class="pl"]/text()').extract()[0].replace('\n','').replace(' ','').replace('人评价','')
            item['descrption'] = bookitem.xpath('//span[@class="inq"]/text()').extract()[0].replace('\n','').replace(' ','')

            print(bookitem)
            yield item

        nexturl=htmlResponse.xpath('//div[@class="article"]//div[@class="paginator"]//span[@class="thispage"]/following-sibling::*[1]')[0].xpath('@href').extract()[0]
        print(nexturl)
        yield Request(nexturl,callback = self.parse)

    # # 初始回调
    # def start_requests(self):
    #     pass
