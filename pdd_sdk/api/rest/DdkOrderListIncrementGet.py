# -*- coding: utf-8 -*-

"""
DdkOrderListIncrementGet.py:
https://open.pinduoduo.com/application/document/api?id=pdd.ddk.order.list.increment.get
最后更新时间段增量同步推广订单信息
按照时间段获取授权多多客下面所有多多客的推广订单信息
"""

from pdd_sdk.api.base import RestApi


class DdkOrderListIncrementGet(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)

        self.crash_gift_order = None  # 是否为礼金订单，查询礼金订单时，订单类型不填（默认推广订单）。

        # 查询结束时间，和开始时间相差不能超过24小时。note：此时间为时间戳，指格林威治时间 1970 年01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数
        self.end_update_time: int = None
        self.page = None  # 第几页，从1到10000，默认1，注：使用最后更新时间范围增量同步时，必须采用倒序的分页方式（从最后一页往回取）才能避免漏单问题。
        self.page_size = None  # 返回的每页结果订单数，默认为100，范围为10到100，建议使用40~50，可以提高成功率，减少超时数量。
        self.query_order_type = None  # 订单类型：1-推广订单；2-直播间订单
        # 是否返回总数，默认为true，如果指定false, 则返回的结果中不包含总记录数，通过此种方式获取增量数据，效率在原有的基础上有80%的提升。
        self.return_count = None
        # 最近90天内多多进宝商品订单更新时间--查询时间开始。note：此时间为时间戳，指格林威治时间 1970 年01 月 01 日 00 时 00 分 00 秒(北京时间 1970 年 01 月 01 日 08 时 00 分 00 秒)起至现在的总秒数
        self.start_update_time: int = None

    def getapiname(self):
        return 'pdd.ddk.order.list.increment.get'
