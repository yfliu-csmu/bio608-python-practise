# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:04:59 2017

@author: Yu-Fan Liu, PH.D.
"""
import re

def read_seq(fn):

    f = open(fn, 'r')
    seq = []                    # define c_seq is empty array object

    for line in f.readlines():
        if not re.match('^>', line):   # remove description lines
           for base in line:
               if not base == '\n':
                   seq += base              
    f.close()
    return seq

def complementary_seq(seq):
    
    c_seq = []                  # define c_seq is empty array object

    c_table = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    
    for base in seq:
        c_seq += c_table[base]

    return c_seq
    
def reverse_seq(c_seq):

    return c_seq[::-1]

def read_t_table(fn):
    
    f = open (fn, 'r')
    t_table = {}                  # define translation table one codon

    for line in f.readlines():
        words = line.rstrip().split(sep=' ')  
        t_table[words[0]] = {'one':words[1], 'three':words[2]}
        
    return t_table  

def translation(seq, offset, t_table):
    
    codon = ""
    protein = []

    for i in range(offset, int(len(seq)/3)*3, 3):
        protein.append(t_table[codon.join(seq[i]+seq[i+1]+seq[i+2])]['one'])
        protein.append(t_table[codon.join(seq[item:item+3])]['one'])

    return protein
      
"""
=== main ===
"""

gene = ''                         #  define gene is empty string object
protein = []

seq = read_seq('TP53.txt')
c_seq = complementary_seq(seq)
r_seq = reverse_seq(c_seq)
t_table = read_t_table('T_Table.txt')

for i in range(3):
    protein = translation(seq, i, t_table)
    print (gene.join(protein))
    protein = translation(r_seq, i, t_table)
    print (gene.join(protein))

# Hello