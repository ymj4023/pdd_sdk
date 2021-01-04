# -*- coding: utf-8 -*-

"""
GoodsCatsGet.py:
https://open.pinduoduo.com/application/document/api?id=pdd.goods.cats.get
商品标准类目接口
获取拼多多标准商品类目信息（请使用pdd.goods.authorization.cats接口获取商家可发布类目）
"""

from pdd_sdk.api.base import RestApi


class GoodsCatsGet(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        #
        self.parent_cat_id = None  # 值=0时为顶点cat_id,通过树顶级节点获取cat树

    def getapiname(self):
        return 'pdd.goods.cats.get'
