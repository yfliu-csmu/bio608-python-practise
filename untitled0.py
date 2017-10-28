# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 11:06:54 2017

@author: Home
"""

import csv

with open('T_table.csv', 'r') as f:
    t_table = dict()
    for words in csv.reader(f, delimiter = '\t'):
        t_table[words[0]] = {'one':words[1], 'three':words[2]}