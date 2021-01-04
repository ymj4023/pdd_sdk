# -*- coding: utf-8 -*-

"""
DdkMallUrlGen.py:
https://open.pinduoduo.com/application/document/api?id=pdd.ddk.mall.url.gen
多多客生成店铺推广链接API
"""

from pdd_sdk.api.base import RestApi


class DdkMallUrlGen(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)

        self.custom_parameters = None  # 自定义参数，为链接打上自定义标签。自定义参数最长限制64个字节。
        self.generate_mall_collect_coupon = None  # 是否生成店铺收藏券推广链接
        self.generate_qq_app = None  # 是否生成qq小程序
        self.generate_schema_url = None  # 是否返回 schema URL
        self.generate_short_url = None  # 是否生成短链接，true-是，false-否
        self.generate_weapp_webview = None  # 是否生成唤起微信客户端链接，true-是，false-否，默认false
        self.mall_id = None  # 店铺id
        self.multi_group = None  # true--生成多人团推广链接 false--生成单人团推广链接（默认false）1、单人团推广链接：用户访问单人团推广链接，可直接购买商品无需拼团。2、多人团推广链接：用户访问双人团推广链接开团，若用户分享给他人参团，则开团者和参团者的佣金均结算给推手
        self.pid = None  # 推广位

    def getapiname(self):
        return 'pdd.ddk.mall.url.gen'
