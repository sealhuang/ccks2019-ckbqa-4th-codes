# -*- coding: utf-8 -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:

"""
Created on Sat Jul  6 16:51:55 2019

@author: cmy
"""

import pickle
import codecs as cs

mention2entity_dic = {}
with cs.open('../pkubase/pkubase-mention2ent.txt', 'r', 'utf-8') as fp:
    mention2entity_dic = {}
    lines = fp.read().split('\n')[0:-1]
    for line in lines:
        if line.strip():
            mention = line.split('\t')[0]
            entity = line.split('\t')[1]
            if mention in mention2entity_dic:
                mention2entity_dic[mention].append(entity)
            else:
                mention2entity_dic[mention]  = [entity]
                
pickle.dump(mention2entity_dic, open('../data/mention2entity_dic.pkl','wb'))

