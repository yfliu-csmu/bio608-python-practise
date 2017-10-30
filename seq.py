# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:04:59 2017

@author: Yu-Fan Liu, PH.D.
"""
import re, csv

def read_seq(fn):

    with open(fn, 'rt') as f:
        seq = list()      
        for line in f.readlines():
            if not re.match('^>', line):   # remove description lines
                for base in line:
                    if not base == '\n':
                        seq.append(base)              
    
    return seq

def complementary_seq(seq):
    
    c_seq = list()

    c_table = {T':'A', 'C':'G', 'G':'C', 'A':'T'}
    
    for base in seq:
        c_seq.append(c_table[base])

    return c_seq
    
def reverse_seq(c_seq):

    return c_seq[::-1]

def read_t_table(fn):
    
    with open('T_table.csv', 'r') as f:
        t_table = dict()
        for words in csv.reader(f, delimiter = '\t'):
            t_table[words[0]] = {'one':words[1], 'three':words[2]}
                
    return t_table

def translation(seq, offset, t_table):
    
    codon = str()
    protein = list()
    
    for item in range(offset, int(len(seq)/3)*3, 3):
        protein.append(t_table[codon.join(seq[item:item+3])]['one'])

    return protein

def orf(protein):
   
    gene = str()
    print (gene.join(protein))
    
      
"""
=== main ===
"""

protein = list()

seq = read_seq('TP53.txt')
c_seq = complementary_seq(seq)
r_seq = reverse_seq(c_seq)
t_table = read_t_table('T_Table.txt')

for item in range(3):
    protein = translation(seq, item, t_table)
    orf(protein)
    protein = translation(r_seq, item, t_table)
    orf(protein)
