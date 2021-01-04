# -*- coding: utf-8 -*-

"""
DdkMerchantListGet.py:
https://open.pinduoduo.com/application/document/api?id=pdd.ddk.merchant.list.get
多多客查店铺列表接口
"""

from pdd_sdk.api.base import RestApi


class DdkMerchantListGet(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        #
        self.cat_id = None  # 商品类目ID，使用pdd.goods.cats.get接口获取
        self.has_clt_cpn = None  # 是否有店铺收藏券 （true 所有；false 必须有券）
        self.has_coupon = None  # 是否有优惠券 （0 所有；1 必须有券。）
        self.mall_id_list = None  # 店铺id
        self.merchant_type_list = None  # 店铺类型
        self.page_number = None  # 分页数
        self.page_size = None  # 每页数量
        # 查询范围0----商品拼团价格区间；1----商品券后价价格区间；2----佣金比例区间；3----优惠券金额区间；4----加入多多进宝时间区间；5----销量区间；6----佣金金额区间
        self.query_range_str = None

        self.range_vo_list = None  # 筛选范围
        self.pid = None  # 推广位id
        self.custom_parameters = None  # 自定义参数，为链接打上自定义标签。自定义参数最长限制64个字节。

    def getapiname(self):
        return 'pdd.ddk.merchant.list.get'
