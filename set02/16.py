# -*- coding: utf-8 -*-
# (16) 括弧表現のうち，括弧の内側がアルファベット大文字の文字列，括弧の左側が漢字の文字列のものを抽出せよ．このとき，括弧の左側の表現と括弧の内側の表現をタブ区切り形式で出力せよ．

import sys
import csv
import re

# [\p{Han}]が使えないようなのでサロゲートペアを使わない漢字だけ...
# \U00002e80-\U00002e99\U00002e9b-\U00002ef3\U00002f00-\U00002fd5\U00003005\U00003007\U00003021-\U00003029\U00003038-\U0000303b\U00003400-\U00004db5\U00004e00-\U00009fcc\U0000f900-\U0000fa6d\U0000fa70-\U0000fad9
re_kanji_capital = re.compile(u'([\U00002e80-\U00002e99\U00002e9b-\U00002ef3\U00002f00-\U00002fd5\U00003005\U00003007\U00003021-\U00003029\U00003038-\U0000303b\U00003400-\U00004db5\U00004e00-\U00009fcc\U0000f900-\U0000fa6d\U0000fa70-\U0000fad9]+)[(（]([A-Z]+)[)）]', re.UNICODE)

for row in csv.reader(sys.stdin):
    tweet = row[5].decode('utf-8')
    match = re_kanji_capital.search(tweet)
    if match:
        out = u'%s\t%s' % (match.group(1), match.group(2))
        print out.encode('utf-8')

