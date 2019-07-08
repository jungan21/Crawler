# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LianjiaspiderPipeline(object):
    def process_item(self, item, spider):
        return item


import csv


class PipelineCsv(object):

    def open_spider(self, spider):
        self.f = open("list.csv", "w", newline='')
        self.fw = csv.writer(self.f)
        self.fw.writerow(['title', 'name', 'house_type', 'area', \
                          'position', 'floor', 'build_time', 'monthly_rental'])

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        self.fw.writerow([item['title'], item['name'], item['house_type'], \
                         item['area'], item['position'], item['floor'], \
                         item['build_time'], item['monthly_rental']])
