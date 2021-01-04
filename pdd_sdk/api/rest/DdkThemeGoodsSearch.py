


"""
DdkThemeGoodsSearch.py:
"""

from pdd_sdk.api.base import RestApi


class DdkThemeGoodsSearch(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        #
        self.theme_id = None  # 主题ID

    def getapiname(self):
        return 'pdd.ddk.theme.goods.search'
