# -*- coding: utf-8 -*-

"""
DdkThemePromUrlGenerate.py:
https://open.pinduoduo.com/application/document/api?id=pdd.ddk.theme.prom.url.generate
多多进宝主题推广链接生成
"""
from pdd_sdk.api.base import RestApi


class DdkThemePromUrlGenerate(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.custom_parameters = None  # 自定义参数，为链接打上自定义标签。自定义参数最长限制64个字节。
        self.generate_mobile = None  # 是否生成手机跳转链接，true-是，false-否
        self.generate_qq_app = None  # 是否生成qq小程序
        self.generate_short_url = None  # 是否生成短链接，true-是，false-否
        self.generate_weapp_webview = None  # 是否生成唤起微信客户端链接，true-是，false-否，默认false
        self.generate_we_app = None  # 是否生成小程序推广
        self.pid = None  # 推广位
        self.theme_id_list = None  # 主题ID列表,例如[1,235]

    def getapiname(self):
        return 'pdd.ddk.theme.prom.url.generate'
