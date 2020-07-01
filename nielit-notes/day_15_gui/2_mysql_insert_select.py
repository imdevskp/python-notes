import MySQLdb as my
from tkinter import *

# tkinter -----------------------------------------------------

mwin=Tk()
mwin.title('MySQL console')

# mysql ---------------------------------------------

def insert_data():
  q=t.get("1.0","end-1c")
  x=q.split()

  if(x[0]=='select'):
   con_o = my.connect('localhost', 'ai', 'ai', 'ai')
   cur_o = con_o.cursor()
   cur_o.execute(q)
   record=cur_o.fetchall()
   for i in record:
    print(i)

  else:
   con_o = my.connect('localhost', 'ai', 'ai', 'ai')
   cur_o = con_o.cursor()
   cur_o.execute(q)
   con_o.commit()
   print('Executed')
 
# tkinter ------------------------------------------------

t=Text(mwin, height=8, width=80)
t.pack()
b = Button(mwin, height=1, width=10, text='Enter', command = lambda : insert_data())
b.pack()

mwin.mainloop() 