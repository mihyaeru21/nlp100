# -*- coding: utf-8 -*-
# (12) 「なう」という文字列で終わるツイートを抽出せよ．

import sys
import csv

for row in csv.reader(sys.stdin):
    tweet = row[5].decode('utf-8')
    if tweet.endswith(u'なう'):
        print tweet.encode('utf-8')

