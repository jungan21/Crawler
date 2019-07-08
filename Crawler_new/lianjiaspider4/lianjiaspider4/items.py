# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Lianjiaspider4Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HouseItem(scrapy.Item):

    title = scrapy.Field()
    area = scrapy.Field()
    monthly_rental = scrapy.Field()
