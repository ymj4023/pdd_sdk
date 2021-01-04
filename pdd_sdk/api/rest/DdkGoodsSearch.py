# -*- coding: utf-8 -*-

"""
DdkGoodsRecommendGet.py:
https://open.pinduoduo.com/application/document/api?id=pdd.ddk.goods.search
多多进宝商品查询
"""

from pdd_sdk.api.base import RestApi


class DdkGoodsSearch(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)

        # 活动商品标记数组，例：[4,7]，4-秒杀，7-百亿补贴，31-品牌黑标，10564-精选爆品-官方直推爆款，10584-精选爆品-团长推荐，24-品牌高佣，20-行业精选，
        # 21-金牌商家，10044-潜力爆品，10475-爆品上新，其他的值请忽略
        self.activity_tags = None

        self.block_cats = None  # 自定义屏蔽一级/二级/三级类目ID，自定义数量不超过20个;使用pdd.goods.cats.get接口获取cat_id
        # 屏蔽商品类目包：1-拼多多小程序屏蔽的类目&关键词;2-虚拟类目;3-医疗器械;4-处方药;5-非处方药
        self.block_cat_packages = None

        self.cat_id = None  # 商品类目ID，使用pdd.goods.cats.get接口获取

        # 自定义参数，为链接打上自定义标签；自定义参数最长限制64个字节；格式为： {"uid":"11111","sid":"22222"} ，其中 uid 为用户唯一标识，可自行加密后传入，
        # 每个用户仅且对应一个标识，必填； sid 为上下文信息标识，例如sessionId等，非必填。该json字符串中也可以加入其他自定义的key。
        self.custom_parameters = None

        self.goods_id_list = None  # 已经废弃，不再支持该功能。建议使用goods_sign_list进行商品查询
        self.goods_sign_list = None  # goodsSign列表，支持通过goodsSign查询商品
        self.is_brand_goods = None  # 是否为品牌商品
        self.keyword = None  # 商品关键词，与opt_id字段选填一个或全部填写
        self.list_id = None  # 翻页时填写前页返回的list_id值
        self.merchant_type = None  # 店铺类型，1-个人，2-企业，3-旗舰店，4-专卖店，5-专营店，6-普通店（未传为全部）
        self.merchant_type_list = None  # 店铺类型数组
        self.opt_id = None  # 商品标签类目ID，使用pdd.goods.opt.get获取
        self.page = 1  # 默认值1，商品分页数
        self.page_size = 100  # 默认100，每页商品数量
        self.pid = None  # 推广位id
        # 筛选范围列表 样例：[{"range_id":0,"range_from":1,"range_to":1500},{"range_id":1,"range_from":1,"range_to":1500}]
        self.range_list = None
        self.sort_type = None  # 排序方式:0-综合排序;1-按佣金比率升序;2-按佣金比例降序;3-按价格升序;4-按价格降序;5-按销量升序;6-按销量降序;7-优惠券金额排序升序;8-优惠券金额排序降序;9-券后价升序排序;10-券后价降序排序;11-按照加入多多进宝时间升序;12-按照加入多多进宝时间降序;13-按佣金金额升序排序;14-按佣金金额降序排序;15-店铺描述评分升序;16-店铺描述评分降序;17-店铺物流评分升序;18-店铺物流评分降序;19-店铺服务评分升序;20-店铺服务评分降序;27-描述评分击败同类店铺百分比升序，28-描述评分击败同类店铺百分比降序，29-物流评分击败同类店铺百分比升序，30-物流评分击败同类店铺百分比降序，31-服务评分击败同类店铺百分比升序，32-服务评分击败同类店铺百分比降序
        self.with_coupon = None  # false返回所有商品，true只返回有优惠券的商品

    def getapiname(self):
        return 'pdd.ddk.goods.search'
