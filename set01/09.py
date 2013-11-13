# -*- coding: utf-8 -*-
# (9) 各行を２コラム目，１コラム目の優先順位で辞書の逆順ソートしたもの（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題は結果が合わなくてもよい）．

import sys

lines = [line.decode('utf-8').rstrip(u'\r\n') for line in sys.stdin.readlines()]
lines = sorted(lines, key = lambda l: l.split(u'\t')[0])
lines = sorted(lines, key = lambda l: l.split(u'\t')[1])

for line in lines:
    print line.encode('utf-8')

