# -*- coding: utf-8 -*-
from tkinter import *
exp=''
def bh1():
 global exp
 exp+='1'
 tv1.set(exp)
def bh2():
 global exp
 exp+='2'
 tv1.set(exp)
def bh3():
 global exp
 exp+='3'
 tv1.set(exp)
def bh4():
 global exp
 exp+='4'
 tv1.set(exp)
def bh5():
 global exp
 exp+='5'
 tv1.set(exp)
def bh6():
 global exp
 exp+='6'
 tv1.set(exp)
def bh7():
 global exp
 exp+='7'
 tv1.set(exp)
def bh8():
 global exp
 exp+='8'
 tv1.set(exp)
def bh9():
 global exp
 exp+='9'
 tv1.set(exp)
def bh0():
 global exp
 exp+='0'
 tv1.set(exp)
def bhp():
 global exp
 exp+='+'
 tv1.set(exp)
def bhs():
 global exp
 exp+='-'
 tv1.set(exp)
def bhm():
 global exp
 exp+='*'
 tv1.set(exp)
def bhd():
 global exp
 exp+='/'
 tv1.set(exp)
def bhe():
 global exp
 exp = str(eval(exp))
 tv1.set(exp)
def bhc():
 global exp
 exp = ''
 tv1.set(exp)
mwin=Tk()
mwin.title('Calculator')
tv1=StringVar()
e1= Entry(mwin, textvariable=tv1)
e1.grid(row=0, columnspan=4)
b1 = Button(mwin, text='1', command=bh1)
b2 = Button(mwin, text='2', command=bh2)
b3 = Button(mwin, text='3', command=bh3)
b4 = Button(mwin, text='4', command=bh4)
b5 = Button(mwin, text='5', command=bh5)
b6 = Button(mwin, text='6', command=bh6)
b7 = Button(mwin, text='7', command=bh7)
b8 = Button(mwin, text='8', command=bh8)
b9 = Button(mwin, text='9', command=bh9)
b0 = Button(mwin, text='0', command=bh0)
bp = Button(mwin, text='+', command=bhp)
bs = Button(mwin, text='-', command=bhs)
bm = Button(mwin, text='*', command=bhm)
bd = Button(mwin, text='/', command=bhd)
be = Button(mwin, text='=', command=bhe)
bc = Button(mwin, text='C', command=bhc)
b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
bp.grid(row=1, column=3)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
bs.grid(row=2, column=3)
b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)
bm.grid(row=3, column=3)
b0.grid(row=4, column=0)
bc.grid(row=4, column=1)
be.grid(row=4, column=2)
bd.grid(row=4, column=3)
mwin.mainloop() 
