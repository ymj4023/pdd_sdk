# -*- coding: utf-8 -*-

"""
DdkOrderDetailGet.py:
https://open.pinduoduo.com/application/document/api?id=pdd.ddk.order.detail.get
查询订单详情
"""

from pdd_sdk.api.base import RestApi


class DdkOrderDetailGet(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.order_sn = None  # 订单号
        self.query_order_type = None  # 订单类型：1-推广订单；2-直播间订单

    def getapiname(self):
        return 'pdd.ddk.order.detail.get'
