#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import jieba
from optparse import OptionParser

jieba.load_userdict('./dict/dict.txt.big')

USAGE = "usage:    python cut.py [file name]"

parser = OptionParser(USAGE)
opt, args = parser.parse_args()
filename = args[0]

if len(args) < 1:
    print(USAGE)
    sys.exit(1)

fo = open(filename, 'r')
lines = fo.read()
fo.close()

print 'jieba.cut(lines):'

arr = jieba.cut(lines)
print '/ '.join(arr)

print '================'
print 'jieba.cut(lines, cut_all=False): '

arr = jieba.cut(lines, cut_all=False)
print '/ '.join(arr)

print '================'
print 'jieba.cut(lines, cut_all=False, HMM=True): '

arr = jieba.cut(lines, cut_all=False, HMM=False)
print '/ '.join(arr)
