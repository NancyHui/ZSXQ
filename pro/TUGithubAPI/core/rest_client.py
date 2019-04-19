import requests
import urllib3
import json as json_parser

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class RestClient(object):
    def __init__(self, api_host, username=None, password=None, token=None):
        self.api_host = api_host
        self.session = requests.session()
        # 两种鉴权方式：
        if username and password:
            self.session.auth = (username, password)
        elif token:
            self.session.headers['Authorization'] = 'token {}'.format(token)

    def get(self, url, **kwargs):
        return self.request(url, 'get', **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, 'post', data, json, **kwargs)

    def head(self, url, **kwargs):
        return self.request(url, 'head', **kwargs)

    def options(self, url, **kwargs):
        return self.request(url, 'options', **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, 'put', data, **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, 'patch', data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, 'delete', **kwargs)

    def request(self, url, method_name, data=None, json=None, **kwargs):
        url = self.api_host + url
        if method_name == 'get':
            return self.session.get(url, **kwargs)
        elif method_name == 'post':
            return self.session.post(url, data, json, **kwargs)
        elif method_name == 'head':
            return self.session.head(url, **kwargs)
        elif method_name == 'options':
            return self.session.options(url, **kwargs)
        elif method_name == 'put':
            return self.session.put(url, data, **kwargs)
        elif method_name == 'patch':
            # 参数传入时，json是一个字典；通过以下方法将字典json转换为json字符串
            if json:
                data = json_parser.dumps(json)
            return self.session.patch(url, data, **kwargs)
        elif method_name == 'delete':
            return self.session.delete(url, **kwargs)


if __name__ == '__main__':
    host = 'https://www.shwzoo.com'
    url1 = '/tools/submit_ajax.ashx?action=user_login'
    url2 = '/tools/submit_ajax.ashx?action=cart_goods_buy'
    rc = RestClient(host)
    r1 = rc.post(url1, data={'txtUserName': 'chn0622@sina.com', 'txtPassword': 'chn432431'}, verify=False)
    print(r1.status_code)
    print(r1.text)

    r2 = rc.post(url2, data={'jsondata': '[{"goods_id":"34","sell_price":"120.00", "quantity":"2", "goods_type":"1","cart_id":"0","tick_time":"2019-04-20","sku":"73453"}]'}, verify=False)
    print(r2.status_code)
    print(r2.text)

    # 不支持username、password的鉴权方式，支持cookie
    # rc = RestClient(host, txtUserName='chn0622@sina.com', txtPassword='chn432431')
    # r2 = rc.post(url2, data={'jsondata': '[{"goods_id":"34","sell_price":"120.00", "quantity":"2", "goods_type":"1","cart_id":"0","tick_time":"2019-04-20","sku":"73453"}]'},verify=False)
    # print(r2.status_code)
    # print(r2.text)


