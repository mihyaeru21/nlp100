# -*- coding: utf-8 -*-
# (17) 人名らしき表現にマッチする正規表現を各自で設計し，抽出せよ．（例えば「さん」「氏」「ちゃん」などの接尾辞に着目するとよい）

import sys
import csv
import re

# 漢字は[一-龠]で...
re_name = re.compile(u'([a-zA-Z0-9_]+|[ぁ-んー]+|[ァ-ンー]+|[ｧ-ﾝﾞﾟ\-]+|[一-龠]+)(?:さん|ｻﾝ|君|氏|ちゃん|ﾁｬﾝ|たん|ﾀｿ)', re.UNICODE)

names = []
for row in csv.reader(sys.stdin):
    tweet = row[5].decode('utf-8')
    names += re_name.findall(tweet)

for name in sorted(set(names)):
    print name.encode('utf-8')
print len(names)

