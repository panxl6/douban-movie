#!/usr/bin/env python3
# coding=utf-8
# author=XingLong Pan
# date=2016-12-06

import pymysql.cursors


class Helper:

    __connection = None

    def __init__(self):
        self.__connect_database()

    def __connect_database(self):
        self.__connection = pymysql.connect(
            host='localhost',
            user='root',
            password='1234567890',
            db='douban',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    def insert_movie(self, movie):
        try:
            with self.__connection.cursor() as cursor:
                sql = "INSERT INTO `movie` (`douban_id`, `title`, `directors`, " \
                      "`scriptwriters`, `actors`, `types`,`release_region`," \
                      "`release_date`,`alias`,`languages`,`duration`,`score`," \
                      "`description`,`tags`,`link`,`posters`) VALUES (%s," \
                      "%s, %s, %s, %s, %s, %s, %s," \
                      "%s, %s, %s, %s, %s, %s, %s, %s);"
                cursor.execute(sql, (
                    movie['douban_id'],         movie['title'],
                    movie['directors'],         movie['scriptwriters'],
                    movie['actors'],            movie['types'],
                    movie['release_region'],    movie['release_date'],
                    movie['alias'],             movie['languages'],
                    movie['duration'],          movie['score'],
                    movie['description'],       movie['tags'],
                    movie['link'],              movie['posters']
                ))
                self.__connection.commit()
        finally:
            pass

    def close_db(self):
        self.__connection.close()
