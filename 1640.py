# 使用session
import requests
import urllib3

# https协议压制警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 正常情况下，加入购物车操作时，请求会在header中加入Cookie传给服务器，服务器根据cookie进行用户判断
# 两次请求用了同一个session，有同一个header（包含cookie信息），即保证第二个请求操作成功
host = 'https://www.shwzoo.com'
session = requests.session()
url = host + '/tools/submit_ajax.ashx?action=user_login'
params = {'txtUserName': 'chn0622@sina.com', 'txtPassword': 'chn432431'}
r = session.post(url, params, verify=False)
print(r.status_code)

url2 = host + '/tools/submit_ajax.ashx?action=cart_goods_buy'
# Fiddler抓包，request-WebForms-Body中可以看到参数信息，每一行为参数字典中的key-value，key和value均为字符串类型
params2 = {
    'jsondata': '[{"goods_id":"34","sell_price":"120.00", "quantity":"2", "goods_type":"1","cart_id":"0","tick_time":"2019-04-13","sku":"73576"}]'}
r2 = session.post(url2, params2, verify=False)
print(r2.status_code)
print(r2.text)
