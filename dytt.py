# 1. 定位到2020必看片
# 2. 从2025必看片中提取到子也米娜的链接地址
# 3. 请求子页面的链接地址，拿到我们想要的下载地址
import requests
import re
domain = "https://www.dytt89.com/"
resp = requests.get(domain, verify=False) # verify=False 去掉安全源代码
resp.encoding = 'gb2312' # 指定字符集
# print(resp.text)

obj1 = re.compile(r"2025必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r"◎片　　名(?P<movie>.*?)<br />.*?"
                  r'<div class=player_list>.*?<ul>.*?<li><a href="(?P<download>.*?)">.*?</a></li>',re.S)
result1 = obj1.finditer(resp.text)
child_href_list = []
# 拿到ul里面的li
# <a></a>表示超链接
for it in result1:
    ul = it.group('ul')
    # print(ul)

    # 提取子页面链接：
    result2 = obj2.finditer(ul)
    for itt in result2:
        child_href = domain + itt.group('href').strip("/")
        child_href_list.append(child_href) # 保存子页面链接

# 提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = 'gb2312'
    # print(child_resp.text)
    result3 = obj3.search(child_resp.text)
    print(result3.group("movie"))
    print(result3.group("download"))
    # break

