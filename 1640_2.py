# 抽象成为类
import requests
import urllib3

# https协议压制警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class RestClient:
    def __init__(self,api_host):
        self.api_host = api_host
        self.session = requests.session()

    def request(self, url, method_name, params):
        url = self.api_host + url
        if method_name == 'post':
            return self.session.post(url, params, verify=False)
        elif method_name == 'get':
            return self.session.get(url)


if __name__ == '__main__':
    host = 'https://www.shwzoo.com'
    url1 = '/tools/submit_ajax.ashx?action=user_login'
    params1 = {'txtUserName': 'chn0622@sina.com', 'txtPassword': 'chn432431'}

    url2 = '/tools/submit_ajax.ashx?action=cart_goods_buy'
    params2 = {
        'jsondata': '[{"goods_id":"34","sell_price":"120.00", "quantity":"2", "goods_type":"1","cart_id":"0","tick_time":"2019-04-13","sku":"73576"}]'}

    rc = RestClient(host)

    r1 = rc.request(url1, 'post', params1)
    print(r1.status_code)

    r2 = rc.request(url2, 'post', params2)
    print(r2.status_code)
    print(r2.text)


