from core.rest_client import RestClient


class Repos(RestClient):
    # 使用关键字参数
    def __init__(self, api_host, **kwargs):
        super(Repos, self).__init__(api_host, **kwargs)

    # def list_the_repositories(self, visibility=None, affiliation=None, type=None, sort=None, direction=None):
    #     params = {'visibility': visibility,
    #               'affiliation': affiliation,
    #               'type': type,
    #               'sort': sort,
    #               'direction': direction}
    #     return self.get('/user/repos', params=params)
    # 简化
    def list_the_repositories(self, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-your-repositories
        """
        return self.get('/user/repos', **kwargs)

    def list_user_repositories(self, username, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-user-repositories
        """
        return self.get('/users/{}/repos'.format(username), **kwargs)


# if __name__ == '__main__':
#     host = 'https://api.github.com'
# #   url = '/user/repos'
#     params = {'username': 'NancyHui', 'password': 'chn432431'}
#     # re = Repos(host, username='NancyHui', password='chn432431')
#     re = Repos(host, **params)
#     response = re.list_the_repositories(url)
#     print(response.text)