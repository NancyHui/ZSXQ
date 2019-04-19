from core.rest_client import RestClient


class Repos(RestClient):
    def __init__(self, api_host, **kwargs):
        super(Repos, self).__init__(api_host, **kwargs)

    # 任意一个接口都是在授权登录之后才会生效的

    def list_your_repo(self, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-your-repositories
        """
        return self.get('/user/repos', **kwargs)

    def list_user_repo(self, username, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-user-repositories
        :param username: username
        """
        return self.get('/users/{}/repos'.format(username), **kwargs)

    def list_organization_repo(self, org, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-organization-repositories
        :param org: org
        """
        return self.get('/orgs/{}/repos'.format(org), **kwargs)

    def list_all_public_repo(self, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-all-public-repositories
        """
        return self.get('/repositories', **kwargs)

    def create_user_repo(self, **kwargs):
        """
        https://developer.github.com/v3/repos/#create
        """
        return self.post('/user/repos', **kwargs)

    def create_organization_repo(self, org, **kwargs):
        """
        https://developer.github.com/v3/repos/#create
        """
        return self.post('/orgs/{}/repos'.format(org), **kwargs)

    def get_repo(self, owner, repo, **kwargs):
        return self.get('/repos/{}/{}'.format(owner, repo), **kwargs)

    def edit_repo(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/#edit
        :param owner: owner
        :param repo: repo
        """
        return self.patch('/repos/{}/{}'.format(owner, repo), **kwargs)

# if __name__ == '__main__':
#     host = 'https://api.github.com'
#     repos = Repos(host, username='NancyHui', password='chn432431')
#     data = {'visibility': 'public'}
#     # repos.list_user_repo()最后调用的方法是get，所以调用时参数应该是get可以接受的参数，即request()可以接受的参数
#     r = repos.list_user_repo(params=data)
#     print(r.status_code)
#     print(r.text)