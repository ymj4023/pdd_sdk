# -*- coding: utf-8 -*-

"""
DdkThemeGoodsSearch.py:
https://open.pinduoduo.com/application/document/api?id=pdd.ddk.theme.goods.search
多多进宝主题商品查询
"""

from pdd_sdk.api.base import RestApi


class DdkThemeGoodsSearch(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        #
        self.theme_id = None  # 主题ID

    def getapiname(self):
        return 'pdd.ddk.theme.goods.search'
