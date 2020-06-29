from pdd_sdk.api.rest.DdkGoodsDetail import DdkGoodsDetail
from pdd_sdk import appinfo
import pprint
pdd_client_id = "xxx"
pdd_client_secret = "xxx"
pid = "xxx" 

req = DdkGoodsDetail()
req.set_app_info(appinfo(appkey=pdd_client_id, secret=pdd_client_secret))
req.pid = pid
req.goods_id_list = [95448118717]
resp = req.getResponse()
pprint.pprint(resp)