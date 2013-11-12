# -*- coding: utf-8 -*-
# (3) 各行の１列目だけを抜き出したものをcol1.txtに，２列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

import sys

col1s, col2s = [], []
for line in sys.stdin:
    decoded = line.decode('utf-8')
    col1, col2 = decoded.rstrip(u'\r\n').split(u'\t')
    col1s.append((col1+u'\n').encode('utf-8'))
    col2s.append((col2+u'\n').encode('utf-8'))

with open('col1.txt', 'w') as f:
    f.writelines(col1s)

with open('col2.txt', 'w') as f:
    f.writelines(col2s)

