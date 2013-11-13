# -*- coding: utf-8 -*-
# (5) 自然数Nをコマンドライン引数にとり，入力のうち先頭のN行だけ．確認にはheadコマンドを用いよ．

import sys

argvs = sys.argv
n = int(argvs[1])
for i in range(n):
    print sys.stdin.readline().rstrip()

