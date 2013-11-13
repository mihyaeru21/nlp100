# -*- coding: utf-8 -*-
# (7) １コラム目の文字列の異なり数（種類数）．確認にはcut, sort, uniq, wcコマンドを用いよ．

import sys

col1s = []
for line in sys.stdin:
    decoded = line.decode('utf-8')
    col1, col2 = decoded.rstrip(u'\r\n').split(u'\t')
    col1s.append(col1)

print len(set(col1s))

