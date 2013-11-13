# -*- coding: utf-8 -*-
# (10) 各行の２コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べよ．ただし，(3)で作成したプログラムの出力（col2.txt）を読み込むプログラムとして実装せよ．確認にはcut, uniq, sortコマンドを用いよ．

import sys
import collections

freq = collections.defaultdict(int)
for line in sys.stdin:
    word = line.decode('utf-8').rstrip(u'\r\n')
    freq[word] += 1

for key, value in sorted(freq.items(), key = lambda kv: kv[1]):
    print key.encode('utf-8'), freq[key]

