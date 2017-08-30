#!/usr/bin/env python3
# coding=utf-8
# author=XingLong Pan
# date=2016-12-17

import configparser

config = configparser.ConfigParser()
config.read('config.ini')
print(config['douban']['user'])
