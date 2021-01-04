
"""
DdkMallGoodsListGet.py:
http://open.pinduoduo.com/#/apidocument/port?id=179

查询店铺商品
"""

from pdd_sdk.api.base import RestApi


class DdkMallGoodsListGet(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.mall_id = None  # 店铺id
        self.page_number = None  # 分页数
        self.page_size = None  # 返回的每页推广位数量

    def getapiname(self):
        return 'pdd.ddk.mall.goods.list.get'
