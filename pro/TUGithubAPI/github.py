from api.repositories.repos import Repos


class Github(object):
    def __init__(self, **kwargs):
        self.api_host = 'https://api.github.com'
        self.repos = Repos(self.api_host, **kwargs)


if __name__ == '__main__':
    # NancyHui token 无法通过代码新建repo,没有给此token权限
    # github = Github(token='')
    github = Github(username='NancyHui', password='***')

    # chn0622 token
    # github = Github(username='chn0622', password='')
    # github = Github(token='')

    username = 'NancyHui'
    orgname = '****'


    # 调用接口的时候，使用**dict，因为最终调用session.py中的request方法（session.get），其没有visibility/direction等这些参数
    # 需要将这些参数写入字典dict中，以params参数传递

    # data1 = {'visibility': 'public', 'direction': 'desc'}
    # r1 = github.repos.list_your_repo(params=data1)
    # print(r1.text)
    # print(r1.status_code)
    #
    # data2 = {'direction': 'desc'}
    # r2 = github.repos.list_user_repo(username=username, params=data2)
    # print(r2.status_code)
    # print(r2.text)
    #
    # data3 = {'sort': 'updated'}
    # r3 = github.repos.list_organization_repo(org='TestUpCommunity', params=data3)
    # print(r3.status_code)
    # print(r3.text)

    # data4 = {'since': '364'}
    # r4 = github.repos.list_all_public_repo(params=data4)
    # print(r4.status_code)
    # print(r4.text)

    # data5 = {
    #     "name": "Hello-World-Test2",
    #     "description": "This is your first repository",
    #     "homepage": "https://github.com",
    #     "private": False,
    #     "has_issues": True,
    #     "has_projects": True,
    #     "has_wiki": True
    # }
    # r5 = github.repos.create_user_repo(json=data5)
    # print(r5.status_code)
    # print(r5.text)

    # post方法可以直接使用“json=一个字典”的调用传参方式
    # data6 = {
    #     "name": "Hello-World-Test2",
    #     "description": "This is your first repository",
    #     "homepage": "https://github.com",
    #     "private": False,
    #     "has_issues": True,
    #     "has_projects": True,
    #     "has_wiki": True
    # }
    # r6 = github.repos.create_organization_repo(org=orgname, json=data6)
    # print(r6.status_code)
    # print(r6.text)

    # r7 = github.repos.get_repo(username, 'Hello-World-Test2')
    # assert r7.status_code == 200
    # print(r7.status_code)
    # print(r7.text)

    data8 = {
        "name": "Hello-World",
        "description": "This is your first repository",
        "homepage": "https://github.com",
        "private": True,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
    }
    r8 = github.repos.edit_repo(username, 'Hello-World-Test2', json=data8)
    print(r8.status_code)
    print(r8.text)
