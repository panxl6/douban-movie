#!/usr/bin/env python3
# coding=utf-8
# author=XingLong Pan
# date=2016-12-05

from bs4 import BeautifulSoup
from parser import Entity


class MovieParser:
    """
    负责从html文档中解析视频实体信息
    """
    __soup = ''
    __movie = Entity.movie

    def __init__(self, html_doc):
        self.__soup = BeautifulSoup(html_doc, 'html.parser')

    def __get_title(self):
        info = self.__soup.find('span', {'property': 'v:itemreviewed'})
        self.__movie['title'] = info.text

    def __get_directors(self):
        info = self.__soup.find('a', {'rel': 'v:directedBy'})
        self.__movie['directors'] = info.text

    def __get_scriptwriters(self):
        pass

    def __get_actors(self):
        info = self.__soup.find_all('a', {'rel': 'v:starring'})
        self.__movie['actors'] = MovieParser.__compose_list(info)

    def __get_types(self):
        info = self.__soup.find_all('span', {'property': 'v:genre'})
        self.__movie['types'] = MovieParser.__compose_list(info)

    def __release_date(self):
        info = self.__soup.find_all('span', {'property': 'v:initialReleaseDate'})
        self.__movie['release_date'] = MovieParser.__compose_list(info)

    def __get_duration(self):
        info = self.__soup.find('span', {'property': 'v:runtime'})
        self.__movie['duration'] = info.text

    def __get_score(self):
        info = self.__soup.find('strong', {'property': 'v:average'})
        self.__movie['score'] = info.text

    def __get_tags(self):
        info = self.__soup.find('div', {'class': 'tags-body'})
        info = info.contents

        tags = ''
        for item in info:
            item = str(item)
            if len(item) < 5:
                continue
            tags += item[item.find('>') + 1: item.find('</')] + ','
        self.__movie['tags'] = tags

    def __get_description(self):
        info = self.__soup.find('span', {'property': 'v:summary'})
        self.__movie['description'] = info.text.replace(' ', '').strip()

    def __get_video_url(self):
        info = self.__soup.find('a', class_='related-pic-video')
        self.__movie['link'] = info.get('href')

    def __get_posters(self):
        info = self.__soup.find_all('img', {'alt': '图片'})

        posters = ''
        for item in info:
            item = str(item)
            posters += item[19: len(item)-3] + ','
        self.__movie['posters'] = posters

    def __get_others(self):
        info = self.__soup.find('div', id='info')
        info = info.contents

        for i in range(0, len(info)):

            if len(str(info[i])) < 10:
                continue
            if str(info[i]).find('语言') != -1:
                self.__movie['languages'] = info[i+1].replace(' / ', ',').strip()
            if str(info[i]).find('制片国家') != -1:
                self.__movie['release_region'] = info[i + 1].replace(' / ', ',').strip()
            if str(info[i]).find('又名') != -1:
                self.__movie['alias'] = info[i + 1].replace(' / ', ',').strip()
            if str(info[i]).find('编剧') != -1:
                item = str(info[i])
                self.__movie['scriptwriters'] = \
                    item[item.find('/">')+3:item.find('</a')]
            i += 1
        pass

    @staticmethod
    def __compose_list(list_):
        result = ''
        for item in list_: result += item.text + ','
        return result

    @staticmethod
    def print_list(list_):
        result = []
        for item_ in list_:
            result.append(item_)
        return result

    def extract_movie_info(self):
        self.__get_title()
        self.__get_directors()
        self.__get_actors()
        self.__get_types()
        self.__get_duration()
        self.__release_date()
        self.__get_score()
        self.__get_tags()
        self.__get_description()
        self.__get_video_url()
        self.__get_posters()
        self.__get_others()

        return self.__movie

