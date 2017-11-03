# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 23:11:03 2017

@author: Y.F. Liu, Ph.D.
"""

import bio608


seq = bio608.read_seq('TP53.txt')
c_seq = bio608.complementary_seq(seq)
r_seq = bio608.reverse_seq(c_seq)
t_table = bio608.read_t_table('T_table.txt')

frames = bio608.translation(seq, t_table)
all_orfs = bio608.determine_orf(frames)
bio608.select_orf(all_orfs)