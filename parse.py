# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on Fri Nov 17 14:47:38 2017

讀卡與成績計算

@author: YF Liu, Professor
"""

import openpyxl, re

fn = 'binfo.TXT'
inf = list()

with open(fn, 'rt') as f:
    for line in f.readlines():
         words = re.split(r'\s+', line)
         id = str(words[0][0:7])
         score = float(words[1])

wb = openpyxl.Workbook()
ws = wb.active

# x=0
for row in inf:
    ws.append(row)


wb.save('test.xlsx')

import pandas as pd

fn = '0601-A.TXT'
id_list = list()
score_list = list()


def get_stats(group):
    return {'count': group.count()}


with open(fn, 'rt') as f:
    for line in f.readlines():
        words = re.split(r'\s+', line)
        id = str(words[0][0:7])
        score = float(words[1])
        id_list.append(id)
        score_list.append(score)

df = pd.DataFrame(score_list, index=id_list, columns=["期中考"])
s = pd.Series(score_list, index=id_list)


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
print(df.期中考[df.期中考 < 60])
#print (df.期中考[(df.期中考 > 60 and df.期中考 < 70)])
print(df.describe())
#df.plot()

#df_aa = pd.read_html('http://www.soc-bdr.org/rds/authors/unit_tables_conversions_and_genetic_dictionaries/genetic_code_tables/')
# print(df_aa)
