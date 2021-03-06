#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# 关键词提取测试程序

import jieba
import jieba.analyse
from optparse import OptionParser

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

USAGE = "usage:    python extract-tags.py [file name] -k [top k]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
opt, args = parser.parse_args()

if len(args) < 1:
    print(USAGE)
    sys.exit(1)

file_name = args[0]

if opt.topK is None:
    topK = 50
else:
    topK = int(opt.topK)

#allowPOS = ('ns', 'n', 'vn', 'v')
allowPOS = ('ns', 'n', 'vn', 'nr', 'nz')
content = open(file_name, 'rb').read()
print content
dict_content = open('./dict/dict.txt.big', 'rb+').read()
jieba.analyse.set_stop_words("dict/stop_words.txt")
jieba.analyse.set_idf_path("dict/idf.txt.big")
tags = jieba.analyse.extract_tags(content,
                                  topK=topK,
                                  withWeight=True,
                                  allowPOS=allowPOS)
for t in tags:
    flag = dict_content.find(t[0])
    if flag < 0:
        print "=====> %s : %f" % t
    else:
        print "%s : %f" % t

print "*" * 40

textRank_tags = jieba.analyse.textrank(content,
                                       topK=topK,
                                       withWeight=True,
                                       allowPOS=allowPOS)
for t in textRank_tags:
    flag = dict_content.find(t[0])
    if flag < 0:
        print "=====> %s : %f" % t
    else:
        print "%s : %f" % t
