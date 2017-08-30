#!/usr/bin/env python3
# coding=utf-8
# author=XingLong Pan
# date=2016-12-06

import pymysql.cursors
import configparser


class DbHelper:

    __connection = None

    def __init__(self):
        self.__connect_database()

    def __connect_database(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.__connection = pymysql.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            db=config['mysql']['db_name'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    def insert_movie(self, movie):
        try:
            with self.__connection.cursor() as cursor:
                sql = "INSERT IGNORE INTO `movie` (`douban_id`, `title`, `directors`, " \
                      "`scriptwriters`, `actors`, `types`,`release_region`," \
                      "`release_date`,`alias`,`languages`,`duration`,`score`," \
                      "`description`,`tags`) VALUES (%s," \
                      "%s, %s, %s, %s, %s, %s, %s," \
                      "%s, %s, %s, %s, %s, %s);"
                cursor.execute(sql, (
                    movie['douban_id'],
                    movie['title'],
                    movie['directors'],
                    movie['scriptwriters'],
                    movie['actors'],
                    movie['types'],
                    movie['release_region'],
                    movie['release_date'],
                    movie['alias'],
                    movie['languages'],
                    movie['duration'],
                    movie['score'],
                    movie['description'],
                    movie['tags']
                ))
                self.__connection.commit()
        finally:
            pass

    def close_db(self):
        self.__connection.close()
