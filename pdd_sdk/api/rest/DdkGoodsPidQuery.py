# -*- coding: utf-8 -*-

"""
DdkGoodsPidQuery.py:
https://open.pinduoduo.com/application/document/api?id=pdd.ddk.goods.pid.query
查询已经生成的推广位信息
"""

from pdd_sdk.api.base import RestApi


class DdkGoodsPidQuery(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.page = None  # 返回的页数
        self.page_size = None  # 返回的每页推广位数量
        self.pid_list = None  # 推广位id列表
        self.status = None  # 推广位状态：0-正常，1-封禁

    def getapiname(self):
        return 'pdd.ddk.goods.pid.query'
