#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-27 21:23
# @Author  : isosky
# @Site    : 
# @File    : dbs_movie.py

import os
import re
import cookielib
import time
import urllib
import urllib2
import requests
from bs4 import BeautifulSoup

# https://movie.douban.com/subject/20495023/comments?sort=time&status=P
# https://movie.douban.com/subject/20495023/comments?start=20&limit=20&sort=time&status=P&percent_type=

# 只能抓取最新100和最热500

temp_url = 'https://movie.douban.com/subject/%s/comments?start=%s&limit=20&sort=%s&status=P&percent_type='

# user agent
hds = [{
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}]

movie_dir = './movie_html'


def movie_spider(movie_id, ts, type):
    if type:
        temp_dir = os.path.join(movie_dir, str(movie_id), ts, 'time')
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        for i in range(5):
            url = temp_url % (movie_id, i * 20, 'time')
            print url
            try:
                req = urllib2.Request(url, headers=hds[i % len(hds)])
                source_code = urllib2.urlopen(req).read()
                plain_text = str(source_code)
                with open(os.path.join(temp_dir, str(i * 20) + '.html'), 'w') as f:
                    f.write(plain_text)
            except (urllib2.HTTPError, urllib2.URLError), e:
                print e
            time.sleep(2)
    else:
        temp_dir = os.path.join(movie_dir, str(movie_id), ts, 'new_score')
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        for i in range(11, 25):
            url = temp_url % (movie_id, i * 20, 'new_score')
            print url
            try:
                req = urllib2.Request(url, headers=hds[0])
                source_code = urllib2.urlopen(req).read()
                plain_text = str(source_code)
                with open(os.path.join(temp_dir, str(i * 20) + '.html'), 'w') as f:
                    f.write(plain_text)
            except (urllib2.HTTPError, urllib2.URLError), e:
                print e
            time.sleep(5)


raw_cookies = 'gr_user_id=519570b8-bf0a-43e7-b7d7-7123fa53b288; bid=9NqQ6rmzEwI; ll="108288"; ct=y; ps=y; _vwo_uuid_v2=C8DDA0C4B072DFBAA007427B095E0A0A|4d124ab60834738d58000280cef4a580; _ga=GA1.2.659945415.1465021533; ap=1; __utmt=1; dbcl2="141842855:/sVszYTVPtc"; ck=KWg5; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1512288201%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DHKLBqo-xMe7OPsbSk0kQlxpnATGZ2gIYQAWoXOQysP7%26wd%3D%26eqid%3Df8be09af000020ee000000035a201480%22%5D; _pk_id.100001.8cb4=cfc0c6dd3972ba42.1465021532.18.1512288201.1512051891.; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utma=30149280.659945415.1465021533.1511790058.1512288128.26; __utmb=30149280.3.10.1512288128; __utmc=30149280; __utmz=30149280.1510402723.24.21.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.14184'

if __name__ == '__main__':
    cookies = {}
    for line in raw_cookies.split(';'):
        key, value = line.split('=', 1)  # 1 代表只分一次，得到两个数据
        cookies[key] = value

    print cookies
    # time_local = time.localtime(time.time())
    # # 转换成新的时间格式(2016-05-05 20:28:54)
    # dt = time.strftime("%Y%m%d_%H%M%S", time_local)
    # movie_spider(20495023, dt, 0, cookies)
    # movie_spider(20495023, dt, 1, cookies)
