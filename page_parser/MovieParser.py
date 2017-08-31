#!/usr/bin/env python3
# coding=utf-8
# author=XingLong Pan
# date=2016-12-05

from bs4 import BeautifulSoup
from page_parser import Entity


class MovieParser:
    """
    负责从html文档中解析视频实体信息

    当然了，你也可以使用Xpath表达式来提取。这里只是为了方便。
    """
    __soup = ''
    __movie = None
    __NOT_FOUND = '页面不存在'
    __html_doc = ''

    def __set_bs_soup(self):

        self.__soup = BeautifulSoup(self.__html_doc, 'html.parser')

    def __is_404_page(self):

        if self.__html_doc.find(self.__NOT_FOUND) != -1:
            return True

        if len(self.__html_doc) < 500:
            return True

        return False

    def __get_title(self):
        try:
            info = self.__soup.find('span', {'property': 'v:itemreviewed'})
            self.__movie['title'] = info.text
        except:
            pass

    def __get_directors(self):
        try:
            info = self.__soup.find('a', {'rel': 'v:directedBy'})
            self.__movie['directors'] = info.text
        except:
            pass

    def __get_scriptwriters(self):

        temp_str = self.__movie['scriptwriters']
        flag_position = temp_str.rfind('>')

        if flag_position > -1:
            self.__movie['scriptwriters'] = temp_str[flag_position+1: len(temp_str)]

    def __get_actors(self):
        try:
            info = self.__soup.find_all('a', {'rel': 'v:starring'})
            info = MovieParser.__compose_list(info)
            self.__movie['actors'] = MovieParser.__trim_last_comma(info)
        except:
            pass

    def __get_types(self):
        try:
            info = self.__soup.find_all('span', {'property': 'v:genre'})
            info = MovieParser.__compose_list(info)
            self.__movie['types'] = MovieParser.__trim_last_comma(info)
        except:
            pass

    def __release_date(self):
        try:
            info = self.__soup.find_all('span', {'property': 'v:initialReleaseDate'})
            info = MovieParser.__compose_list(info)
            self.__movie['release_date'] = MovieParser.__trim_last_comma(info)
        except:
            pass

    def __get_duration(self):
        try:
            info = self.__soup.find('span', {'property': 'v:runtime'})
            self.__movie['duration'] = info.text
        except:
            pass

    def __get_score(self):
        try:
            info = self.__soup.find('strong', {'property': 'v:average'})
            self.__movie['score'] = info.text
        except:
            pass

    def __get_tags(self):
        try:
            info = self.__soup.find('div', {'class': 'tags-body'})
            info = info.contents

            tags = ''
            for item in info:
                item = str(item)
                if len(item) < 5:
                    continue
                tags += item[item.find('>') + 1: item.find('</')] + ','
            self.__movie['tags'] = MovieParser.__trim_last_comma(tags)
        except:
            pass

    def __get_description(self):
        try:
            info = self.__soup.find('span', {'property': 'v:summary'})
            self.__movie['description'] = info.text.replace(' ', '').strip()
        except:
            pass

    def __get_posters(self):
        try:
            info = self.__soup.find_all('img', {'alt': '图片'})

            posters = ''
            for item in info:
                item = str(item)
                posters += item[19: len(item)-3] + ','
            self.__movie['posters'] = posters
        except:
            pass

    def __get_others(self):
        try:
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
        except:
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

    @staticmethod
    def __trim_last_comma(string):

        if not string:
            return None

        if string[-1] == ',':
            return string[: -1]

    def set_html_doc(self, html_doc):

        self.__html_doc = html_doc

    def extract_movie_info(self):
        """
        如果为404或其他出错页面，返回None。
        :return: None|dict
        """

        if self.__html_doc is None:
            return None

        if self.__is_404_page():
            return None

        print(self.__html_doc)

        self.__set_bs_soup()

        self.__movie = Entity.movie.copy()
        self.__get_title()
        self.__get_directors()
        self.__get_actors()
        self.__get_types()
        self.__get_duration()
        self.__release_date()
        self.__get_score()
        self.__get_tags()
        self.__get_description()
        self.__get_others()
        self.__get_scriptwriters()

        return self.__movie

