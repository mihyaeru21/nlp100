# -*- coding: utf-8 -*-
# (6) 自然数Nをコマンドライン引数にとり，入力のうち末尾のN行だけ．確認にはtailコマンドを用いよ．

import sys

n = int(sys.argv[1])
lines = sys.stdin.readlines()
for line in lines[-n:]:
    print line,

