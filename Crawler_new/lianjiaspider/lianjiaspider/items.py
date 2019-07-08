# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):

    # 标题
    title = scrapy.Field()
    # 小区名
    name = scrapy.Field()
    # 户型
    house_type = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 所在位置
    position = scrapy.Field()
    # 房子楼层
    floor = scrapy.Field()
    # 房子建筑时间
    build_time = scrapy.Field()
    # 月租金
    monthly_rental = scrapy.Field()
