# -*- coding: utf-8 -*-
import scrapy
from lianjiaspider.items import HouseItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/zufang/']

    def parse(self, response):
        item = HouseItem()
        for box in response.xpath('//ul[@class="house-lst"]/li'):
            item['title'] = box.xpath('.//div[2]/h2/a/@title').extract()[0]
            item['name'] = box.xpath('.//div[2]/div[1]/div[1]/a/span/text()').extract()[0]
            item['house_type'] = box.xpath('.//div[2]/div[1]/div[1]/span[1]/span/text()').extract()[0]
            item['area'] = box.xpath('.//div[2]/div[1]/div[1]/span[2]/text()').extract()[0]
            item['position'] = box.xpath('.//div[2]/div[1]/div[2]/div/a/text()').extract()[0]
            item['floor'] = box.xpath('.//div[2]/div[1]/div[2]/div').xpath('string(.)').extract()[0].split('/')[1]
            item['build_time'] = box.xpath('.//div[2]/div[1]/div[2]/div').xpath('string(.)').extract()[0].split('/')[2]
            item['monthly_rental'] = box.xpath('.//div[2]/div[2]/div[1]/span/text()').extract()[0]
            yield item
