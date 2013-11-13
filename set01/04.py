# -*- coding: utf-8 -*-
# (4) (3)で作ったcol1.txtとcol2.txtを結合し，元のタブ区切りテキストを復元したもの．確認にはpasteコマンドを用いよ．

import sys

with open('col1.txt') as f:
    col1s = f.readlines()

with open('col2.txt') as f:
    col2s = f.readlines()

for i in range(len(col1s)):
    print '%s\t%s' % (col1s[i].rstrip(), col2s[i].rstrip())

