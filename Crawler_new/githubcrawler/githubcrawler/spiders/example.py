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

        if (text.find ("Scotiabank111") | text.find ("Toronto") ):
            print ("FOUND IT!!!!!!!!!!!")

       # piiInfo = soup.body.findAll(text='autoandr')
        #print(soup.get_text().find("Scotiabank111"))

        #info = soup.find_all('label', {'name': 'em_weixinhao'})


       # profile_link = soup.find_all(uigs='account_image_0')[0]['href']

       # file = open('./gzh_info.txt', 'w')
        #file.write('weixinhao: ' + info[0].string + '\n')
        #file.write(profile_link)
        #file.close()

       # yield Request(profile_link, callback=self.parse_profile)



    '''
    解析公众号的Profile界面获取10个历史文章信息
    '''
    def parse_profile(self, response):
        results = []

        articles = article_list_re.findall(response.text)
        if not articles:
            return []
        articles = articles[0] + '}}]}'
        articles = json.loads(articles)
        for article in articles['list']:
            if str(article['comm_msg_info'].get('type', '')) != '49':
                continue

            comm_msg_info = article['comm_msg_info']
            app_msg_ext_info = article['app_msg_ext_info']
            datetime = comm_msg_info.get('datetime', '')
            type = str(comm_msg_info.get('type', ''))

            results.append({
                'datetime': datetime,
                'type': type,
                'main': 1,
                'title': app_msg_ext_info.get('title', ''),
                'abstract': app_msg_ext_info.get('digest', ''),
                'fileid': app_msg_ext_info.get('fileid', ''),
                'content_url': 'https://mp.weixin.qq.com' + self.__replace_str_html(
                    app_msg_ext_info.get('content_url')),
                'source_url': app_msg_ext_info.get('source_url', ''),
                'cover': app_msg_ext_info.get('cover', ''),
                'author': app_msg_ext_info.get('author', ''),
                'copyright_stat': app_msg_ext_info.get('copyright_stat', '')
            })

            if app_msg_ext_info.get('is_multi', 0) == 1:
                for multi_dict in app_msg_ext_info['multi_app_msg_item_list']:
                    results.append({
                        'datetime': datetime,
                        'type': type,
                        'main': 0,
                        'title': multi_dict.get('title', ''),
                        'abstract': multi_dict.get('digest', ''),
                        'fileid': multi_dict.get('fileid', ''),
                        'content_url': ('https://mp.weixin.qq.com' +
                                        self.__replace_str_html(multi_dict.get('content_url'))),
                        'source_url': multi_dict.get('source_url', ''),
                        'cover': multi_dict.get('cover', ''),
                        'author': multi_dict.get('author', ''),
                        'copyright_stat': multi_dict.get('copyright_stat', '')
                    })
        file = open('./history_article_link.txt', 'w')
        for item in results:
            if item['content_url'] != '':
                yield Request(url=item['content_url'], callback=self.get_article)
                file.write(item['content_url'] + '\n')
        file.close()

    def get_article(self, response):
        soup = BeautifulSoup(response.text, features='lxml')
        title = soup.select('.rich_media_title')
        # 文章是转载的
        if not title:
            return

        item = WechatCrawlerItem()
        title_pattern = re.compile('var msg_title = "(.*)";')
        title = title_pattern.findall(response.text)[0]
        title = title.strip('\r').strip('\n').strip(' ')

        item['title'] = title
        item['link'] = response.url
        item['content'] = response.text

        file = open('./content/%s' % title, 'w')
        file.write(item['content'])
        file.close()

    @staticmethod
    def __replace_str_html(content):
        transfer = [
            ('&#39;', '\''),
            ('&quot;', '"'),
            ('&amp;', '&'),
            ('amp;', ''),
            ('&lt;', '<'),
            ('&gt;', '>'),
            ('&nbsp;', ' '),
            ('\\', '')
        ]
        for item in transfer:
            content = content.replace(item[0], item[1])
        return content
