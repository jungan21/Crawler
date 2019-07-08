# -*- coding: utf-8 -*-
import scrapy
from lianjiaspider4.items import HouseItem
from scrapy import Request


class ExampleSpider(scrapy.Spider):
    name = 'example' # use to start the scrapy crawler i.e.: scrapy crawl example
    allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/zufang']

    def parse(self, response):
        # response.txt
        # Note:  only parse 1st page of the webiste
        url = 'https://bj.lianjia.com/zufang'
        yield Request(url, callback=self.parse_item)

        # Note:   parse 2 - 5 page of the webiste
        for num in range (2, 5):
            url = 'https://bj.lianjia.com/zufang/pg%s' % num
            yield Request(url, callback=self.parse_item)


    # Note:  only parse 1st page of the webiste
    def parse_item(self, response):
        # response.txt
        box = response.xpath('//*[@id="content"]/div[1]/div[1]')
        for num in range(1, 20):
            item = HouseItem()
            item['title'] = box.xpath('./div[%s]/div/p[1]/a/text()' % num).extract()[0]
            item['area'] = box.xpath('./div[%s]/div/p[2]/text()[2]' % num).extract()[0]
            item['monthly_rental'] = box.xpath('./div[%s]/div/span/em/text()' % num).extract()[0]
            yield item # yield 是个生成器




    # below lines of code will print out the captured text content
    #def parse(self, response):
    #    print(response.text)
    #    pass

    # another method
    #def parse2(self, response):
    #    # response.txt
    #    for box in response.xpath('//*[@id="content"]/div[1]/div[1]'):
    #        item = HouseItem()
    #        item['title'] = box.xpath('./div[1]/div/p[1]/a/text()').extract()[0]
    #        item['area'] = box.xpath('./div[1]/div/p[2]/text()[2]').extract()[0]
    #        item['monthly_rental'] = box.xpath('./div[1]/div/span/em/text()').extract()[0]


