# -*- coding: utf-8 -*-

"""
DdkThemeListGet.py:
https://open.pinduoduo.com/application/document/api?id=pdd.ddk.theme.list.get
查询多多进宝主题列表
"""

from pdd_sdk.api.base import RestApi


class DdkThemeListGet(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        #
        self.page = None  # 返回的页码
        self.page_size = None  # 返回的一页数据数量

    def getapiname(self):
        return 'pdd.ddk.theme.list.get'
