# -*- coding: utf-8 -*-
from collections import OrderedDict
from urllib import parse


_search_gzh = 1
_search_article = 2


class SogouRequest:

    # 生成搜索公众号主页的链接
    @classmethod
    def generate_search_gzh_url(cls, keyword):

        query = OrderedDict()
        query['type'] = _search_gzh
        query['ie'] = 'utf8'
        query['query'] = keyword

        return 'http://weixin.sogou.com/weixin?%s' % parse.urlencode(query)


if __name__ == '__main__':
    url = SogouRequest.generate_search_gzh_url('九章算法')
    print(url)