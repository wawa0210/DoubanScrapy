# -*- coding: utf-8 -*-
import scrapy

from douban.items import JianshuItem


class JianshuSpider(scrapy.Spider):
    name = 'jianshu'
    allowed_domains = ['http://www.jianshu.com']
    start_urls = ['http://www.jianshu.com/']

    def parse(self, response):

        # print(response.body)

        selector=scrapy.Selector(response)

        articles=selector.xpath('//ul[@class="note-list"]/li')

        for article in articles:
            item = JianshuItem()
            jianshu = article.xpath('div[@class="content"]')
            authorhtml = jianshu.xpath('div[@class="author"]')

            item['title'] = jianshu.xpath('a/text()').extract()[0]
            item['url'] = ""
            item['author'] = authorhtml.xpath('div[@class="name"]/a/text()').extract()[0]
            item['readNum'] = jianshu.xpath('div[@class="meta"]/a/text()').extract()[2].replace('\n','').replace(' ','')
            item['commentNum'] =jianshu.xpath('div[@class="meta"]/a/text()').extract()[4].replace('\n','').replace(' ','')
            item['likeNum'] = jianshu.xpath('div[@class="meta"]/span/text()').extract()[0].replace('\n','').replace(' ','')
            item['deccrption'] = jianshu.xpath('p[@class="abstract"]/text()').extract()[0].replace('\n','').replace(' ','')


            yield item

