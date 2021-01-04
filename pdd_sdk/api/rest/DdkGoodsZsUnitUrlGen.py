# -*- coding: utf-8 -*-

"""
DdkGoodsZsUnitUrlGen.py:
https://open.pinduoduo.com/application/document/api?id=pdd.ddk.goods.zs.unit.url.gen
多多进宝转链接口

本功能适用于采集群等场景。将其他推广者的推广链接转换成自己的；
通过此api，可以将他人的招商推广链接，转换成自己的招商推广链接
"""

from pdd_sdk.api.base import RestApi


class DdkGoodsZsUnitUrlGen(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.pid: int = None  # 推广位id
        self.source_url = None  # 需转链的链接

        # 自定义参数，为链接打上自定义标签；自定义参数最长限制64个字节；格式为： {"uid":"11111","sid":"22222"} ，其中 uid 用户唯一标识，可自行加密后传入，每个用户仅且对应一个标识，必填；
        # sid 上下文信息标识，例如sessionId等，非必填。该json字符串中也可以加入其他自定义的key
        self.custom_parameters = None

    def getapiname(self):
        return 'pdd.ddk.goods.zs.unit.url.gen'
