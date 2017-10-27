# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 01:09:41 2017

@author: Y.F. Liu, Ph.D.
"""
cc = dict()

for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            if i+j+k in cc:
                cc[i+j+k] += 1
            else:
                cc[i+j+k] = 1
      
for x in range(3,19):
    print(x, ":", round(cc[x]*100/(6*6*6), 2), "%")

