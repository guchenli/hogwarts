# -*- coding: utf-8 -*-

#  mitmdump
from mitmproxy import http

# # request 函数名不能修改，是固定的
# def request(flow: http.HTTPFlow) -> None:
#     # 请求URL，判断url是不是预期的路径
#     if flow.request.pretty_url == "https://www.baidu.com/":
#         #如果url是我们预期的，我们就会创建一个response
#         flow.response = http.HTTPResponse.make(
#                 200,  # (optional) status code
#                 b"hello guchenli",  # (optional) content
#                 {"Content-Type": "text/html"}  # (optional) headers
#             )
#
#
# request 函数名不能修改，是固定的
def request(flow: http.HTTPFlow) -> None:
    # 判断返回的文件在文件中
    if "quote.json" in flow.request.pretty_url:
        #打开保存在本地的文件
        with open("C:/Users/guchenli/Desktop/quote.json", encoding="utf-8") as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                #读取文件中数据作为返回内容
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )