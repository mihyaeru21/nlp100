# -*- coding: utf-8 -*-
# (15) ツイッターのユーザー名（例えば@xxxxxxx）を，そのユーザーのページへのリンク（<a href="https://twitter.com/#!/xxxxxxx">@xxxxxxx</a>で囲まれたHTML断片）に置換せよ．

import sys
import csv
import re

re_name = re.compile(u'@([a-zA-Z0-9_]+)')

for row in csv.reader(sys.stdin):
    tweet = row[5].decode('utf-8')
    replaced = re_name.sub(ur'<a href="https://twitter.com/#!/\1">@\1</a>', tweet)
    if replaced != tweet:
        print replaced.encode('utf-8')

