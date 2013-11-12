# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:
    decoded = line.decode('utf-8')
    print decoded.rstrip().replace(u'\t', u' ').encode('utf-8')

