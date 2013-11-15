# -*- coding: utf-8 -*-
# (13) 非公式RTのツイートの中で，RT先へのコメント部分のみを抽出せよ．
# 非公式RTの形式を '[comment] RT @screen_name: [original_tweet]' として実装した

import sys
import csv
import re

re_rt = re.compile(u'(\A\w+) RT @[a-zA-Z0-9_]+: ', re.UNICODE)

for row in csv.reader(sys.stdin):
    tweet = row[5].decode('utf-8')
    match = re_rt.search(tweet)
    if match:
        print match.group(1).encode('utf-8')

