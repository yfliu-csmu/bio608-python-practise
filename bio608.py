# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:04:59 2017

@author: Yu-Fan Liu, PH.D.
"""
import re, csv,  pprint

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

def translation(seq, t_table):
    """進行轉譯 DNA 序列 (包含正反兩股的 6 個 Frames)"""
    codon = str()
    all = dict()
    
    for frame in range(3):
      protein = list()
      for item in range(frame, int(len(seq)/3)*3, 3):
        protein.append(t_table[codon.join(seq[item:item+3])]['one'])
      all['positive strain frame-'+str(frame+1)] = protein
    
    c_seq = complementary_seq(seq)
    r_seq = reverse_seq(c_seq)

    for frame in range(3):
      protein = list()
      for item in range(frame, int(len(r_seq)/3)*3, 3):
        protein.append(t_table[codon.join(seq[item:item+3])]['one'])
      all['negative strain frame-'+str(frame+1)] = protein
 
    return all

def determine_orf(frames):
    """判斷每個 Frames 的開放式框架 (ORFs) """
    all = dict()
    
    for info, protein in frames.items():
      orfs = list()
      long = 0
      num = 0
      for pp in ''.join(protein).split('*'):
        for x in range(len(pp)):
          if (pp[x] == 'M'):
            orfs.append(pp[x:len(pp)])
            num += 1
            if (len(pp)-x+1) > long:
              long = len(pp)-x+1     
            break
      all[info] = {'orfs': orfs, 'num': num, 'long': long}    
    
    return all
          
def select_orf(all):
    """選擇正確的 Protein 框架"""
    pp = pprint.PrettyPrinter(depth=3)
    pp.pprint(all)
          