# coding=utf-8
# author=XingLong Pan
# date=2016-11-07

import time
import random


class Utils:

    @staticmethod
    def delay(min_second, max_second):
        time.sleep(random.randrange(min_second, max_second))
