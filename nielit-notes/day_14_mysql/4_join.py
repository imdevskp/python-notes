import MySQLdb as my

con_o = my.connect('localhost', 'ai', 'ai', 'ai')
cur_o = con_o.cursor()

q = '''
        select ai17_items.tid, name, stock-temp.sm as balance
        from ai17_items 
        inner join (select tid, sum(qty) sm from ai17_sales group by tid) as temp 
        on ai17_items.tid=temp.tid;
'''

cur_o.execute(q)
result = cur_o.fetchall()
for i in result:
 print(i)
