# -*- coding: utf-8 -*-
# (11) 「拡散希望」という文字列を含むツイートを抽出せよ．

import sys
import csv

for row in csv.reader(sys.stdin):
    tweet = row[5].decode('utf-8')
    if u'拡散希望' in tweet:
        print tweet.encode('utf-8')

