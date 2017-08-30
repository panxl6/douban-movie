#!/usr/bin/env python3
# coding=utf-8
# author=XingLong Pan
# date=2016-12-24

import csv


class CsvHelper:

    columns = ['id', 'douban_id', 'title', 'directors',
               'scriptwriters', 'actors', 'types', 'release_region',
               'alias', 'languages', 'duration', 'score', 'description',
               'tags']

    def __init__(self):

        print('--------------------------')
        self._csv_file = open('douban_movie.csv', 'w', newline='')
        self._writer = csv.writer(self._csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        self._writer.writerow(CsvHelper.columns)

    def write_row(self, line):
        try:
            self._writer.writerow(line)
        except IOError as e:
            print(e)

    def close(self):
        self._csv_file.close()
