# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 18:02:12 2017

@author: YF Liu
"""
sequence = str()
gb =list()

start_pos = sequence.find('GCCGCCACCATG')
print ("START " + str(start_pos))
if start_pos >= 0:
    s_to_ATG = int(start_pos) + 9
    start = sequence[s_to_ATG:]
    xrange = list()
    for i in xrange(0, len(start), 3):
        stops =["TAA", "TGA", "TAG"]
        codon = start[i:i+3]
        if codon in stops:
            orf = start[:i+3]
            break
        else:
            orf = start
                
elif start_pos < 0:
    stop_pos = sequence.find(str(gb[-12:]))
    begin_to_stop = int(stop_pos) + 12
else:
    print ("Error: There is no open-reading frame for this sequence!")