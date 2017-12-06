#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-3 15:40
# @Author  : isosky
# @Site    : 
# @File    : pss.py


# -*- coding: utf-8 -*-
import cookielib
import urllib2

__author__ = 'jason'
import requests
# import html5lib
import cookielib
import urllib2
import re
from bs4 import BeautifulSoup

s = requests.Session()
url_login = 'https://accounts.douban.com/login'

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)

formdata = {
    'redir': 'https://www.douban.com',
    'form_email': '18601025057',
    'form_password': 'zhutou1234',
    'login': u'登陆'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

r = urllib2.Request(url_login, data=formdata, headers=headers)
print r
t = urllib2.urlopen(r)
content = t.text
soup = BeautifulSoup(content, 'html.parser')
captcha = soup.find('img', id='captcha_image')  # 当登陆需要验证码的时候
if captcha:
    captcha_url = captcha['src']
    re_captcha_id = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
    captcha_id = re.findall(re_captcha_id, content)
    print(captcha_id)
    print(captcha_url)
    captcha_text = raw_input('Please input the captcha:')
    formdata['captcha-solution'] = captcha_text
    formdata['captcha-id'] = captcha_id
    r = urllib2.Request(url_login, data=formdata, headers=headers)
    t = urllib2.urlopen(r).read()

# content = r.text
print 'aa'
cookie.save(ignore_discard=True, ignore_expires=True)
print content

# cookie = cookielib.CookieJar()
# #利用 urllib2 库的 HTTPCookieProcessor 对象来创建 cookie 处理器
# handler=urllib2.HTTPCookieProcessor(cookie)
# #通过 handler 来构建 opener
# opener = urllib2.build_opener(handler)
# #此处的 open 方法同 urllib2 的 urlopen 方法，也可以传入 request
# response = opener.open('https://www.douban.com')
# for item in cookie:
#     print 'Name ='+item.name
#     print 'Value ='+item.value

# with open('contacts.txt', 'w+') as f:
#     f.write(r.text)


# filename = 'cookie.txt'
# #声明一个 MozillaCookieJar 对象实例来保存 cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postdata = urllib.urlencode({
#             'stuid':'201200131012',
#             'pwd':'23342321'
#         })
# #登录教务系统的 URL
# loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
# #模拟登录，并把 cookie 保存到变量
# result = opener.open(loginUrl,postdata)
# #保存 cookie 到 cookie.txt 中
# cookie.save(ignore_discard=True, ignore_expires=True)
# #利用 cookie 请求访问另一个网址，此网址是成绩查询网址
# gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
# #请求访问成绩查询网址
# result = opener.open(gradeUrl)
# print result.read()