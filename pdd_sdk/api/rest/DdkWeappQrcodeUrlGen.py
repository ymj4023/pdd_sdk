# -*- coding: utf-8 -*-

"""
DdkWeappQrcodeUrlGen.py:
https://open.pinduoduo.com/application/document/api?id=pdd.ddk.weapp.qrcode.url.gen
多多客生成单品推广小程序二维码url
"""


from pdd_sdk.api.base import RestApi


class DdkWeappQrcodeUrlGen(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)

        self.cash_gift_id = None  # 多多礼金ID
        self.custom_parameters = None  # 自定义参数，为链接打上自定义标签；自定义参数最长限制64个字节
        self.generate_mall_collect_coupon = None  # 是否生成店铺收藏券推广链接

        self.goods_id_list = None  # 商品ID，仅支持单个查询
        self.goods_sign_list = None  # goodsSign列表，仅支持单个商品
        self.p_id = None  # 推广位id
        self.room_id_list = None  # 直播间id列表，如果生成直播间推广链接该参数必填，goods_id_list填[1]
        # 直播预约id列表，如果生成直播间预约推广链接该参数必填，goods_id_list填[1]，room_id_list不填
        self.target_id_list = None

        self.zs_duo_id = None  # 招商多多客ID

    def getapiname(self):
        return 'pdd.ddk.weapp.qrcode.url.gen'
