# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import csv

# PipelineCsv 必须在 settings.py定义
class PipelineCsv(object):

    def open_spider(self, spider):
        # 如果要写入图片 打开方式必须是 "wb" which means binary
        self.f = open("list.csv", "w", newline='')
        self.fw = csv.writer(self.f)
        self.fw.writerow(['title', 'area', 'monthly_rental']) # csv file title

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        self.fw.writerow([item['title'], item['area'], \
                          item['monthly_rental']])
