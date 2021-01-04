# -*- coding: utf-8 -*-

"""
DdkGoodsDetail.py:
https://open.pinduoduo.com/application/document/api?id=pdd.ddk.goods.detail
多多进宝商品详情查询
"""

from pdd_sdk.api.base import RestApi


class DdkGoodsDetail(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)

        self.custom_parameters = None  # 自定义参数
        # 商品ID，仅支持单个查询，例如：[123456]。建议使用goods_sign进行查询
        self.goods_id_list = None
        self.goods_sign = None  # 商品goodsSign，支持通过goods_sign查询商品。优先使用此字段进行查询
        self.pid = None  # 推广位id
        self.plan_type = None  # 佣金优惠券对应推广类型，3：专属 4：招商
        # 搜索id，建议填写，提高收益。来自pdd.ddk.goods.recommend.get、pdd.ddk.goods.search、pdd.ddk.top.goods.list.query等接口
        self.search_id = None
        self.zs_duo_id = None  # 招商多多客ID

    def getapiname(self):
        return 'pdd.ddk.goods.detail'
