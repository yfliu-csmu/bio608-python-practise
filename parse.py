# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:47:38 2017

讀卡與成績計算

@author: YF Liu, Professor
"""

import openpyxl

fn = 'binfo.TXT'
inf = list()

with open(fn, 'rt') as f:
    for line in f.readlines():
        words = line.split(sep=' ')
        id = words[0][0:7]
        score = words[41][0:-1]
        if words[46] == '':
            ans = words[47]
        else:
            ans = words[46]
        inf.append([str(id), score])
        
wb = openpyxl.Workbook()
ws = wb.active

#x=0
for row in inf:
    ws.append(row)
  


wb.save('test.xlsx')


