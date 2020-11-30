# -*- coding: utf-8 -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:

"""
Created on Sat Jun 29 16:40:36 2019

@author: cmy
"""

import pickle

prop_dic = pickle.load(open('../data/prop_dic.pkl', 'rb'))

char_2_prop = {}

for prop in prop_dic:
    # 这里设置最大长度，不考虑长度过长的属性值
    if len(prop)<20:
        chars = set(prop)
        for char in chars:
            try:
                char_2_prop[char].append(prop)
            except:
                char_2_prop[char] = [prop]
            
pickle.dump(char_2_prop, open('../data/char_2_prop.pkl', 'wb'))

