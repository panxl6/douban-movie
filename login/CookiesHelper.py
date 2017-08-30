#!/usr/bin/env python3
# coding=utf-8
# author=XingLong Pan
# date=2016-12-04

import constants
import requests
from login import Entity
from bs4 import BeautifulSoup
from PIL import Image


class CookiesHelper:
    """
    通过实现模拟登录，获取cookies。
    """

    __user_name = ''
    __password = ''
    __captcha_id = ''
    __captcha_solution = ''
    __is_captcha_exist = True

    def __init__(self, username, password):
        self.__user_name = username
        self.__password = password

    def __get_captcha(self):

        # 获取验证码图片的url
        r = requests.post(constants.DOUBAN_MOVIE_LOGIN_URL,
                          data=Entity.login_form)
        soup = BeautifulSoup(r.text)
        captcha = soup.find_all(id='captcha_image')

        # 如果没有验证码，更新标志位状态并退出函数
        if len(captcha) == 0:
            self.__is_captcha_exist = False
            return

        captcha_url = captcha[0]['src']

        # 获取验证码的id
        self.__captcha_id = captcha_url[
                                captcha_url.find('=') + 1: captcha_url.find(':', 6) + 3
                            ]

        # 下载验证码图片并保存到当前目录
        captcha_image = open('captcha.jpg', 'wb')
        captcha_request = requests.get(captcha_url)
        captcha_image.write(captcha_request.content)
        captcha_request.close()

    def __get_user_input(self):

        if self.__user_name is None or self.__password is None:
            print('请输入注册邮箱：')
            self.__user_name = input()

            print('请输入密码：')
            self.__password = input()

        if self.__is_captcha_exist:
            print('请输入图中的验证码:')
            Image.open('captcha.jpg').show()
            self.__captcha_solution = input()

    def get_cookies(self):

        self.__get_captcha()
        self.__get_user_input()

        data = Entity.login_form
        data['form_email'] = self.__user_name
        data['form_password'] = self.__password
        data['captcha-id'] = self.__captcha_id
        data['captcha-solution'] = self.__captcha_solution

        session = requests.Session()
        session.post(
            constants.DOUBAN_MOVIE_LOGIN_URL,
            data=data
        )

        return session.cookies.get_dict()
