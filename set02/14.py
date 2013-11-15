# -*- coding: utf-8 -*-
# (14) ツイッターのユーザー名（@で始まる文字列）を抽出せよ．
# Twitter公式の「全てのツイートをダウンロードする」から得たデータには、
# ユーザ名の欄が無いので、全tweetからユーザ名を抽出する

import sys
import csv
import re

re_name = re.compile(u'@([a-zA-Z0-9_]+)')

names = []
for row in csv.reader(sys.stdin):
    tweet = row[5].decode('utf-8')
    names += re_name.findall(tweet)

for name in sorted(set(names)):
    print name

