# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:04:59 2017

@author: Yu-Fan Liu, PH.D.
"""
import re, csv

def read_seq(fn):
    """讀取 DNA 序列"""
    with open(fn, 'rt') as f:
        seq = list()      
        for line in f.readlines():
            if not re.match('^>', line):   # remove description lines
                for base in line:
                    if not base == '\n':
                        seq.append(base)              
    
    return seq

def complementary_seq(seq):
    """互補 DNA 序列"""
    c_seq = list()

    c_table = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    
    for base in seq:
        c_seq.append(c_table[base])

    return c_seq
    
def reverse_seq(c_seq): 
    """反轉 DNA 序列"""
    c_seq.reverse()
    
    return c_seq

def read_t_table(fn):
    """建立 Translation Table"""
    with open('T_table.csv', 'r') as f:
        t_table = dict()
        for words in csv.reader(f, delimiter = '\t'):
            t_table[words[0]] = {'one':words[1], 'three':words[2]}
                
    return t_table

def translation(seq, offset, t_table):
    """進行轉譯 DNA 序列"""
    codon = str()
    protein = list()
    
    for item in range(offset, int(len(seq)/3)*3, 3):
        protein.append(t_table[codon.join(seq[item:item+3])]['one'])

    return protein

def orf(protein):
    """判斷 Protein 框架"""
    gene = str()
    print (gene.join(protein))