# -*- coding: utf-8 -*-

"""
DdkMallGoodsListGet.py:
https://open.pinduoduo.com/application/document/api?id=pdd.ddk.mall.goods.list.get
查询店铺商品
"""

from pdd_sdk.api.base import RestApi


class DdkMallGoodsListGet(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.mall_id = None  # 店铺id
        self.page_number = None  # 分页数
        self.page_size = None  # 返回的每页推广位数量
        self.pid = None  # 推广位id
        # 自定义参数，为链接打上自定义标签；自定义参数最长限制64个字节；格式为： {"uid":"11111","sid":"22222"} ，其中 uid 用户唯一标识，可自行加密后传入，每个用户仅且对应一个标识，必填；
        # sid 上下文信息标识，例如sessionId等，非必填。该json字符串中也可以加入其他自定义的key
        self.custom_parameters = None

    def getapiname(self):
        return 'pdd.ddk.mall.goods.list.get'
