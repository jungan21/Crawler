# -*- coding: utf-8 -*-
from collections import OrderedDict
from urllib import parse


_search_gzh = 1
_search_article = 2


class SogouRequest:

    # 生成搜索公众号主页的链接
    @classmethod
    def generate_search_gzh_url(cls, keyword): # self 表示对象所有的方法， cls表示类所有的方法 调用的时候：SogouRequest.generate_search_gzh_url(u'九章算法')

        query = OrderedDict()
        query['type'] = _search_gzh
        query['ie'] = 'utf8'
        query['query'] = keyword

        return 'http://weixin.sogou.com/weixin?%s' % parse.urlencode(query)


#用于调试， 不会被外面调用
if __name__ == '__main__':
    url = SogouRequest.generate_search_gzh_url('九章算法')
    print(url)