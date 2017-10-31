# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 13:32:44 2017

@author: Y.F. Liu, Ph.D.
"""

from tkinter import Tk, Label, Button

wnd = Tk()
count = 0

def clickOK():
  global count
  count += 1
  label2.configure(text='你按 OK 鍵 '+str(count)+' 次')

wnd.title('我第一個 GUI 程式')
wnd.geometry('280x80+500+300')

label1  = Label(wnd, text='我是標簽 1', bg='skyblue')
label2  = Label(wnd, text='我是標籤 2', bg='yellow')
button1 = Button(wnd, text='OK', width=20, bg='pink', command=clickOK)


label1.pack()
label2.pack()
button1.pack(side='bottom')

wnd.mainloop()