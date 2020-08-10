
from pdd_sdk.api.base import RestApi

class DdkGoodsRecommendGet(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.channel_type = 1  # 0-1.9包邮, 1-今日爆款, 2-品牌清仓,3-相似商品推荐,4-猜你喜欢,5-实时热销,6-实时收益,7-今日畅销,8-高佣榜单，默认1

        #自定义参数，为链接打上自定义标签；自定义参数最长限制64个字节；格式为： {"uid":"11111","sid":"22222"} ，其中 uid 用户唯一标识，可自行加密后传入，
        # 每个用户仅且对应一个标识，必填； sid 上下文信息标识，例如sessionId等，非必填。该json字符串中也可以加入其他自定义的key
        self.custom_parameters = None
        self.limit = 400    # 请求数量；默认值 ： 400
        self.list_id = None  #  翻页时建议填写前页返回的list_id值
        self.offset = 0 # 从多少位置开始请求；默认值 ： 0，offset需是limit的整数倍，仅支持整页翻页
        self.pid = None    # 推广位id

        # 猜你喜欢场景的商品类目，20100-百货，20200-母婴，20300-食品，20400-女装，20500-电器，20600-鞋包，20700-内衣，20800-美妆，20900-男装，
        # 21000-水果，21100-家纺，21200-文具,21300-运动,21400-虚拟,21500-汽车,21600-家装,21700-家具,21800-医药;
        self.cat_id = None
        self.goods_ids = None    # 相似商品推荐场景时必传。商品Id，请求相似商品时，仅取数组的第一位

    def getapiname(self):
        return 'pdd.ddk.goods.recommend.get'
