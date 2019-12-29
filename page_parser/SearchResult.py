#!/usr/bin/env python3
# coding=utf-8
# author=XingLong Pan
# date=2016-12-05

from bs4 import BeautifulSoup
import requests


class SearchResult:
    """
    从搜索结果页面提取url
    """

    __keyword = ''
    __page_total = 0
    __current_page = 1
    __page_size = 15
    __search_url = 'https://movie.douban.com/subject_search?search_text='
    __result_url = 'https://movie.douban.com/subject_search?start='

    def __init__(self, keyword):
        self.__keyword = keyword
        self.__get_page_total()

    def __get_page_total(self):
        r = requests.get(self.__search_url + self.__keyword)
        soup = BeautifulSoup(r.text, 'html.parser')
        total = soup.find('span', {'class': 'count'}).text

        if len(total) > 4:
            self.__page_total = int(total[2:len(total) - 2])

    def get_page_links(self):

        if self.__page_total == 0:
            return None

        url = self.__result_url + str(self.__current_page * self.__page_size) + '&search_text=' + self.__keyword
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        soup = soup.find('div', {'class': 'grid-16-8 clearfix'})
        links = soup.find_all('a', {'class': ''})

        result, counter = [], 0
        for item in links:
            counter += 1
            if counter > self.__page_size:
                break
            result.append(str(item.get('href')))

        if self.__current_page < self.__page_size * self.__page_total:
            self.__current_page += 1
            return result
        return None
