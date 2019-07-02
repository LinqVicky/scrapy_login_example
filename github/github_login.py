# -*- coding: utf-8 -*-

"""
github登录
info:
author:
update_time:2019-7-2
"""

import requests
from lxml import etree


class Login(object):

    def __init__(self, email, password):

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Referer': 'https://github.com/',
            'Host': 'github.com'
        }

        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.session = requests.Session()

        self.email = email
        self.password = password


    def login_GitHub(self):
    """
    模拟登录
    """
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.get_token(),
            'login': self.email,
            'password': self.password
        }

        response = self.session.post(self.post_url, data=post_data, headers=self.headers)

        print(response.status_code)
        print(post_data)

        if response.status_code == 200:
            print("登录成功！")
        else:
            print("登录失败！")

 
    def get_token(self):
    """
    获取token信息
    """
        response = self.session.get(self.login_url, headers=self.headers)

        html = etree.HTML(response.content.decode())

        token = html.xpath('//input[@name="authenticity_token"]/@value')[0]

        return token


if __name__ == '__main__':
    email = input('请输入您的账号： ')
    password = input('请输入您的密码： ')

    login = Login(email, password)
    login.login_GitHub()
