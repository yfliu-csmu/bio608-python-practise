# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 13:32:44 2017

@author: Y.F. Liu, Ph.D.
"""

from tkinter import Tk, Label, Button, Entry, StringVar

wnd = Tk()
v = StringVar()

### Step 1 - DNA complementary sequence from seq
def complementary_seq(seq):
    """互補 DNA 序列"""    
    c_seq = list()

    c_table = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    
    for base in seq:
        c_seq += c_table[base]

    return c_seq

### Step 2 - Define click OK button command
def clickOK():
  """定義按鍵 OK 的功能""" 
  seq = list()
  ss = str()

  for base in entry1.get():
    seq.append(base)
  r_seq = seq[::-1]
  c_seq = complementary_seq(r_seq)
  ss = "5'-" + ''.join(c_seq) + "-3'"
  v.set(ss)

wnd.title('我第二個 GUI 程式')
wnd.geometry('300x80+500+300')

label1  = Label(wnd, text='請輸入 DNA 序列 ', bg='skyblue')
label2  = Label(wnd, text='顯示互補的 DNA 序列 ', bg='pink')
entry1  = Entry(wnd)
entry2  = Entry(wnd, textvariable=v)
button1 = Button(wnd, text='執行', command=clickOK)

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
button1.grid(row=2, columnspan=2)

wnd.mainloop()



