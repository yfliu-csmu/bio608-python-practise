# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 20:10:22 2017

@author: Home
cats"""

import pandas as pd

fn = '0601-A.TXT'
id_list = list()
score_list = list()

def get_stats(group):
    return {'count': group.count()}

with open(fn, 'rt') as f:
  for line in f.readlines():
    words = line.split(sep=' ')
    id = str(words[0][0:7])
    score = float(words[41])
    id_list.append(id)
    score_list.append(score)
    
df = pd.DataFrame(score_list, index = id_list, columns = ["期中考"])
sd = pd.Series(score_list)



bins = [40, 50, 60, 70, 80, 90, 100]

cats = pd.cut(df['期中考'], bins, right=False)
grouped = df['期中考'].groupby(cats)
bin_counts = grouped.apply(get_stats).unstack()
print(bin_counts)

bin_counts.index = ['40~50', '50~60', '60~70',
                    '70~80', '80~90', '90~100']
bin_counts.index.name = 'Score range'
bin_counts.plot(kind='bar', alpha=0.5, rot=0)

#print (sd[sd < 70 and sd > 60])
print (df.期中考[df.期中考 < 60])
#print (df.期中考[(df.期中考 > 60 and df.期中考 < 70)])
print (df.describe())
df.plot()



