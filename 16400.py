import requests, json, urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class RestClient:
    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.session()

    def get(self, url, **kwargs):
        return self.request(url, "get", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "post", data, json, **kwargs)

    def options(self, url, **kwargs):
        return self.request(url, "potions", **kwargs)

    def head(self, url, **kwargs):
        return self.request(url, "head", **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, "put", data, **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, "patch", data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "delete", **kwargs)

    def request(self, url, method_name, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        if method_name == "get":
            return self.session.get(url, **kwargs)
        if method_name == "post":
            return self.session.post(url, data, json, **kwargs, verify=False)
        if method_name == "options":
            return self.session.options(url, **kwargs)
        if method_name == "head":
            return self.session.head(self, url, **kwargs)
        if method_name == "put":
            return self.session.put(self, url, data, **kwargs)
        if method_name == "patch":
            return self.session.patch(self, url, data, **kwargs)
        if method_name == "delete":
            return self.session.delete(self, url, **kwargs)


if __name__ == '__main__':
    host = 'https://www.shwzoo.com'
    url1 = '/tools/submit_ajax.ashx?action=user_login'
    params1 = {'txtUserName': 'chn0622@sina.com', 'txtPassword': 'chn432431'}

    url2 = '/tools/submit_ajax.ashx?action=cart_goods_buy'
    params2 = {
        'jsondata': '[{"goods_id":"34","sell_price":"120.00", "quantity":"2", "goods_type":"1","cart_id":"0","tick_time":"2019-04-13","sku":"73576"}]'}
    r = RestClient(host)
    l1 = r.post(url1, data=params1)
    print(l1.status_code)
    l2 = r.post(url2, data=params2)
    print(l2.status_code)
    print(l2.text)