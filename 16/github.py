from api.repositories.repos import Repos


class Github(object):
    def __init__(self, **kwargs):
        self.api_host = 'https://api.github.com'
        self.re = Repos(self.api_host, **kwargs)


if __name__ == '__main__':
    params1 = {'username': 'NancyHui', 'password': 'chn432431'}
    params2 = {'token': '2c3932b65d33ea569d3b8335a9cfbcbd23cd0df5'}
    git = Github(**params1)
    # 与git = Github(**params)效果相同，因为rest_client类中的初始化方法中有username、password、token这三个参数。
    # git = Github(username='NancyHui', password='chn432431')

    # response = git.re.list_the_repositories(visibility='private')
    params3 = {'visibility': 'private', 'direction': 'desc'}
    # 此处不能使用**params，因为最终调用session.py中的request方法（session.get）没有visibility/direction这些参数
    # def request(self, method, url,
    #         params=None, data=None, headers=None, cookies=None, files=None,
            # auth=None, timeout=None, allow_redirects=True, proxies=None,
            # hooks=None, stream=None, verify=None, cert=None, json=None)
    response = git.re.list_the_repositories(params=params3)
    print(response.status_code)
    print(response.text)

    response2 = git.re.list_user_repositories('zhangting85')
    print(response2.status_code)
    print(response2.text)



