# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 23:11:03 2017

@author: Y.F. Liu, Ph.D.
"""

import bio608

protein = list()

seq = bio608.read_seq('TP53.txt')
c_seq = bio608.complementary_seq(seq)
r_seq = bio608.reverse_seq(c_seq)
t_table = bio608.read_t_table('T_Table.txt')

for item in range(3):
    protein = bio608.translation(seq, item, t_table)
    bio608.orf(protein)
    protein = bio608.translation(r_seq, item, t_table)
    bio608.orf(protein)