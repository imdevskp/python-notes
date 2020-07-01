import MySQLdb as my

con_o = my.connect('localhost', 'ai', 'ai', 'ai')
cur_o = con_o.cursor()

q1 = '''
        create table ai17_items(tid int, name char(20), price int, stock int, primary key(tid));
'''
q2 = '''
        create table ai17_sales(tid int, region char(20), qty int);
'''

cur_o.execute(q1)
cur_o.execute(q2)
print('Created')
