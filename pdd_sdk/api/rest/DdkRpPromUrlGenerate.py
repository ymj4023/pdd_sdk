# -*- coding: utf-8 -*-

"""
DdkRpPromUrlGenerate.py:
https://open.pinduoduo.com/application/document/api?id=pdd.ddk.rp.prom.url.generate
生成营销工具推广链接
"""

from pdd_sdk.api.base import RestApi


class DdkRpPromUrlGenerate(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.amount = None  # 初始金额（单位分），有效金额枚举值：300、500、700、1100和1600，默认300
        # -1-活动列表，0-默认红包，2–新人红包，3-刮刮卡，5-员工内购，6-购物车，7-大促会场，8-直播间列表集合页，10-生成绑定备案链接，11-生成超级红包（仅支持微信小程序），12-砸金蛋
        self.channel_type = None
        self.custom_parameters = None  # 自定义参数，为链接打上自定义标签。自定义参数最长限制64个字节。
        self.diy_lottery_param = None  # 转盘自定义参数
        self.range_items = None  # 自定义价格和商品佣金区间
        self.diy_red_packet_param = None  # 红包自定义参数
        self.generate_qq_app = None  # 是否生成qq小程序
        self.generate_schema_url = None  # 是否返回 schema URL
        self.generate_short_url = None  # 是否生成短链接，true-是，false-否
        self.generate_we_app = None  # 是否生成小程序推广
        self.p_id_list = None  # 推广位列表，例如：["60005_612"]

    def getapiname(self):
        return 'pdd.ddk.rp.prom.url.generate'
