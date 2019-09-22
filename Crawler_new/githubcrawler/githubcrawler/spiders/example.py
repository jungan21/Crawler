# -*- coding: utf-8 -*-
import scrapy

from bs4 import BeautifulSoup
from scrapy import Request

import json
import re


article_list_re = re.compile('var msgList = (.*?)}}]};')


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['github.com']
    start_urls = ["https://github.com/stevechae?tab=repositories"]

    def parse(self, response):
        # Write your code here
        soup = BeautifulSoup(response.text, features='lxml')
        text = soup.get_text()

        if (text.find ("Account") | text.find ("Password") | text.find ("account number") | text.find("scotiabank")):
            print ("FOUND IT!!!!!!!!!!!")

      