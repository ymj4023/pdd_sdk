# -*- coding: utf-8 -*-

"""
DdkGoodsPidGenerate.py:
https://open.pinduoduo.com/application/document/api?id=pdd.ddk.goods.pid.generate
创建多多进宝推广位
"""

from pdd_sdk.api.base import RestApi


class DdkGoodsPidGenerate(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.number = None  # 要生成的推广位数量，默认为10，范围为：1~100
        self.p_id_name_list = None  # 推广位名称，例如["1","2"]
        self.media_id = None  # 媒体id

    def getapiname(self):
        return 'pdd.ddk.goods.pid.generate'
