# 类中封装方法
import requests
import urllib3

# https协议压制警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class RestClient:
    def __init__(self, api_host):
        self.api_host = api_host
        self.session = requests.session()

    # 在RestClient类中封装session的请求方法，
    # 封装时，与session中的方法名和参数是一致的
    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, 'post', data, json, **kwargs)

    def get(self, url, **kwargs):
        return self.request(url, **kwargs)

    def option(self, url, **kwargs):
        return self.request(url, **kwargs)

    def head(self, url, **kwargs):
        return self.request(url, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, data, **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, **kwargs)

    def request(self, url, method_name, data=None, json=None, **kwargs):
        url = self.api_host + url
        if method_name == 'post':
            return self.session.post(url, data, json, **kwargs, verify=False)
        elif method_name == 'get':
            return self.session.get(url, **kwargs)
        elif method_name == 'option':
            return self.session.options(url, **kwargs)
        elif method_name == 'head':
            return self.session.head(url, **kwargs)
        elif method_name == 'put':
            return self.session.put(url, data, **kwargs)
        elif method_name == 'patch':
            return self.session.patch(url, data, **kwargs)
        elif method_name == 'delete':
            return self.session.delete(url, **kwargs)


if __name__ == '__main__':
    host = 'https://www.shwzoo.com'
    url1 = '/tools/submit_ajax.ashx?action=user_login'
    params1 = {'txtUserName': 'chn0622@sina.com', 'txtPassword': 'chn432431'}

    url2 = '/tools/submit_ajax.ashx?action=cart_goods_buy'
    params2 = {
        'jsondata': '[{"goods_id":"34","sell_price":"120.00", "quantity":"2", "goods_type":"1","cart_id":"0","tick_time":"2019-04-13","sku":"73576"}]'}

    rc = RestClient(host)
    r1 = rc.post(url1, params1)
    print(r1.status_code)

    r2 = rc.post(url2, data=params2)
    print(r2.status_code)
    print(r2.text)


