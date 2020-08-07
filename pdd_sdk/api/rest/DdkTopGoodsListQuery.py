# -*- coding: utf-8 -*-

"""
DdkTopGoodsListQuery.py:

https://open.pinduoduo.com/application/document/api?id=pdd.ddk.top.goods.list.query
多多客获取爆款排行商品接口
"""


from pdd_sdk.api.base import RestApi


class DdkTopGoodsListQuery(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.limit = 400  # 请求数量；默认值 ： 400
        self.list_id = ""  # 翻页时建议填写前页返回的list_id值
        self.offset = 0  # 从多少位置开始请求；默认值 ： 0
        self.pid = ""  # 推广位id
        self.sort_type = 1  # 1-实时热销榜；2-实时收益榜

        # 自定义参数，为链接打上自定义标签；自定义参数最长限制64个字节；格式为： {"uid":"11111","sid":"22222"} ，
        # 其中 uid 用户唯一标识，可自行加密后传入，每个用户仅且对应一个标识，必填； sid 上下文信息标识，例如sessionId等，非必填。
        # 该json字符串中也可以加入其他自定义的key
        self.custom_parameters = ""

    def getapiname(self):
        return 'pdd.ddk.top.goods.list.query'