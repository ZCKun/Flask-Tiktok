import time
import math

ORIGION='JP'
COUNT="10"
TIMESTAMP=str(math.floor(time.time()*1000))
RESOLUTION="1920*1080"


PARAMS = {
    "type": "0",
    "max_cursor": "0",
    "min_cursor": "-1",
    "count": COUNT, # 加载个数
    "volume": "0.2",
    "pull_type": "2",
    "req_from": "",
    "gaid": "",
    "ad_user_agent": "Dalvik%2F2.1.0+%28Linux%3B+U%3B+Android+6.0.1%3B+MuMu+Build%2FV417IR%29", # 广告ua
    "filter_warn": "0",
    "ts": TIMESTAMP[:-3], # 时间戳
    "js_sdk_version": "",
    "app_type": "normal",
    "os_api": "28",
    "device_type": "Xiaomi",
    "ssmix": "a",
    "manifest_version_code": "9999",
    "dpi": "240",
    "carrier_region": "JP", # 获取的小视频来源
    "region": "JP",
    "carrier_region_v2": "",
    "app_name": "trill",
    "version_name": "4.2.4",
    "ab_version": "4.2.4",
    "timezone_offset": "28800",
    "pass-route": "1",
    "pass-region": "1",
    "is_my_cn": "0",
    "fp":"",
    #"fp": "R2TrcrUtFMsrFYQZcrU1LSFeFWm1",
    "ac": "wifi",
    "update_version_code": "4240",
    "channel": "googleplay",
    "_rticket": TIMESTAMP, # 时间戳（保留毫秒）
    "device_platform": "android",
    "iid":"6678981313393919746", # 暂不知来源，必须有，不能更改
#     "iid": "6678981313393919746",
    "build_number": "9.5",
    "version_code": "424",
    "timezone_name": "Asia%2FShanghai",
    "openudid": "c55cd951e5464a56",
    "device_id": "6678979145927919106",
    "sys_region": "JP",
    "app_language": "zh-Hans",
    "resolution": RESOLUTION, # 画质
#     "resolution": "1280*720",
    "os_version": "9",
    "device_brand": "Android",
    "language": "jp",
    "aid": "1180", # 暂不知来源，必须有，不能更改
    "mcc_mnc": "",
    "as": "",
    "cp":"",
    "mas":""
    #"as": "a10548abb2087cfbe04299",
    #"cp": "8c8fc35c2606b9bae1Wc_g",
    #"mas": "019e07c3ae4fc3d6e172de9de34998f0ae9c9c4c2c0ca64666c6ec"
}
