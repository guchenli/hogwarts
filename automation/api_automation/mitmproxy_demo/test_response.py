# -*- coding: utf-8 -*-
from mitmproxy import http
import json

def response(flow: http.HTTPFlow):
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 使用 json 里 的loads方法，把响应数据变成 json 结构体
        data = json.loads(flow.response.content)
        data['data']['items'][0]['quote']['name'] = "hogwarts0000001"
        data['data']['items'][1]['quote']['name'] = "second"
        data['data']['items'][1]['quote']['current'] = 100000
        flow.response.text = json.dumps(data)