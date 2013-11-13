# -*- coding: utf-8 -*-
# (8) 各行を２コラム目の辞書順にソートしたもの（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題は結果が合わなくてもよい）．

import sys

lines = [line.decode('utf-8').rstrip(u'\r\n') for line in sys.stdin.readlines()]
lines = sorted(lines, key = lambda l: l.split(u'\t')[1])

for line in lines:
    print line.encode('utf-8')


