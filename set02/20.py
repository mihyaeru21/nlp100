# -*- coding: utf-8 -*-
# (20) ツイートから絵文字らしき文字列を抽出せよ．

import sys
import csv
import re

# 絵文字？顔文字？
face = ur"([(（][｀´*][`'・^＾+｀´][Aω∀д_][`'・^＾+｀´][｀´*][)）])"
re_face = re.compile(face, re.UNICODE)

faces = []
for row in csv.reader(sys.stdin):
    tweet = row[5].decode('utf-8')
    faces += re_face.findall(tweet)

for face in sorted(set(faces)):
    print face.encode('utf-8')

