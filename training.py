# -*- coding: utf-8 -*-
"""
Bio606 Python Training Course
Y.F. Liu, Ph.D.
2017.11.1
"""

import re
import csv
import pprint

### Step 1 - read input DNA sequence from plain text file 'TP53.txt'
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


seq = read_seq('TP53.txt')

### Step 2 - DNA complementary sequence from seq
def complementary_seq(seq):
    """互補 DNA 序列"""
    c_seq = list()

    c_table = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    for base in seq:
        c_seq.append(c_table[base])

    return c_seq


### Step 3 - Reverse the DNA sequence from c_seq
def reverse_seq(c_seq):
    """反轉 DNA 序列"""
    c_seq.reverse()

    return c_seq


### Step 4 - Create the codon table of DNA -> Protein from csv file 'T_table.csv'
def read_t_table(fn):
    """建立 Translation Table"""
    with open('T_table.csv', 'r') as f:
        t_table = dict()
        for words in csv.reader(f, delimiter='\t'):
            t_table[words[0]] = {'one': words[1], 'three': words[2]}

    return t_table


t_table = read_t_table('T_table.txt')

### Step 5 - Translation the six reading frames from DNA double strains
def translation(seq, t_table):
    """進行轉譯 DNA 序列 (包含正反兩股的 6 個 Frames)"""
    codon = str()
    frames = dict()

    for frame in range(3):
        protein = list()
        for item in range(frame, int(len(seq) / 3) * 3, 3):
            protein.append(t_table[codon.join(seq[item:item + 3])]['one'])
        frames['positive strain frame-' + str(frame + 1)] = protein

    c_seq = complementary_seq(seq)
    r_seq = reverse_seq(c_seq)

    for frame in range(3):
        protein = list()
        for item in range(frame, int(len(r_seq) / 3) * 3, 3):
            protein.append(t_table[codon.join(r_seq[item:item + 3])]['one'])
        frames['negative strain frame-' + str(frame + 1)] = protein

    return frames


frames = translation(seq, t_table)

### Step 6 - Determine the ORFs and generate info of these ORFs (longest orf and its lenght)
def determine_orf(frames):
    """ 判斷每個 Frames 的開放式框架 (ORFs)，
        記錄每個 Frames 上所有的開放式框架，和最長的開放式框架與長度 """
    all_orfs = dict()

    for info, protein in frames.items():
        orfs = list()
        longest = 0
        candidate = 0
        num = 0
        for pp in (''.join(protein).split('*')):
            if ('M' in pp):
                x = pp.index('M')
                orfs.append(pp[x:])
                if (len(pp) - x) > longest:
                    longest = len(pp) - x
                    candidate = num
                num += 1
        all_orfs[info] = {'orfs': orfs,
                          'candidate': candidate,
                          'longest': longest}
    return all_orfs


all_orfs = determine_orf(frames)

### Step 7 - Select the real ORF for the gene (TP53)
def select_orf(all):
    """選擇正確的 Protein 框架"""
    pp = pprint.PrettyPrinter(depth=3)
    pp.pprint(all)


select_orf(all_orfs)
