#!/usr/bin/env python3
# coding=utf-8
# author=XingLong Pan
# date=2016-12-04

"""
定义登录模块中所用到的实体类型
"""

import constants

# 登录验证表单的结构
login_form = {
    'source': 'movie',
    'redir': 'https://movie.douban.com/',
    'form_email': 'test',
    'form_password': 'test',
    'captcha-solution': '',
    'captcha-id': '',
    'remember': 'on',
    'login': '登录'
}

user_agent = {'User-Agent': constants.USER_AGENT}
