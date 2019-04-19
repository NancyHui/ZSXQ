# 类中封装方法
import requests
import urllib3

# https协议压制警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class RestClient:
    def __init__(self, api_host, username=None, password=None, token=None):
        self.api_host = api_host
        self.session = requests.session()
        # 用户名和密码登录的实现
        if username and password:
            self.session.auth = (username, password)
        # token登录的实现
        elif token:
            self.session.headers['Authorization'] = 'token {}'.format(token)
        print(self.session.headers)

    # 在RestClient类中封装session的请求方法，
    # 封装时，与session中的方法名和参数是一致的
    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, 'post', data, json, **kwargs)

    def get(self, url, **kwargs):
        return self.request(url, 'get', **kwargs)

    def option(self, url, **kwargs):
        return self.request(url, 'option', **kwargs)

    def head(self, url, **kwargs):
        return self.request(url, 'head', **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, 'put', data, **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, 'patch', data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, 'delete',**kwargs)

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






