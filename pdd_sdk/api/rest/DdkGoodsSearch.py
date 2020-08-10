"""
DdkGoodsSearch.py:

https://open.pinduoduo.com/#/apidocument/port?id=27
多多进宝商品查询
"""

from pdd_sdk.api.base import RestApi


class DdkGoodsSearch(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)

        self.activity_tags = None # 商品活动标记数组，例：[4,7]，4-秒杀 7-百亿补贴等
        self.cat_id = None  # 商品类目ID，使用pdd.goods.cats.get接口获取
        self.custom_parameters = None  # 自定义参数
        self.goods_id_list = None  # 商品ID列表。例如：[123456,123]，当入参带有goods_id_list字段，将不会以opt_id、 cat_id、keyword维度筛选商品
        self.is_brand_goods = None # 是否为品牌商品
        self.keyword = None  # 商品关键词，与opt_id字段选填一个或全部填写
        self.list_id = None  # 翻页时填写前页返回的list_id值
        self.merchant_type = None  # 店铺类型，1-个人，2-企业，3-旗舰店，4-专卖店，5-专营店，6-普通店（未传为全部）
        self.merchant_type_list = None # 店铺类型数组
        self.opt_id = None # 商品标签类目ID，使用pdd.goods.opt.get获取
        self.page = 1 # 默认值1，商品分页数
        self.page_size = 100  # 默认100，每页商品数量
        self.pid = None  # 推广位id
        self.range_list = None  #	筛选范围列表 样例：[{"range_id":0,"range_from":1,"range_to":1500},{"range_id":1,"range_from":1,"range_to":1500}]
        self.sort_type = None  # 排序方式:0-综合排序;1-按佣金比率升序;2-按佣金比例降序;3-按价格升序;4-按价格降序;5-按销量升序;6-按销量降序;7-优惠券金额排序升序;8-优惠券金额排序降序;9-券后价升序排序;10-券后价降序排序;11-按照加入多多进宝时间升序;12-按照加入多多进宝时间降序;13-按佣金金额升序排序;14-按佣金金额降序排序;15-店铺描述评分升序;16-店铺描述评分降序;17-店铺物流评分升序;18-店铺物流评分降序;19-店铺服务评分升序;20-店铺服务评分降序;27-描述评分击败同类店铺百分比升序，28-描述评分击败同类店铺百分比降序，29-物流评分击败同类店铺百分比升序，30-物流评分击败同类店铺百分比降序，31-服务评分击败同类店铺百分比升序，32-服务评分击败同类店铺百分比降序
        self.with_coupon = None  # false返回所有商品，true只返回有优惠券的商品            
        self.custom_parameters = None  # 自定义参数

    def getapiname(self):
        return 'pdd.ddk.goods.search'
