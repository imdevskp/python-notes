import MySQLdb as my

con_o = my.connect('localhost', 'ai', 'ai', 'ai')
cur_o = con_o.cursor()

f = open('items.csv', 'r')
cont = f.readlines()
# print(cont)

for row in cont[1:]:
 i = row.split(',')
 tid = int(i[0])
 name = i[1]
 price = int(i[2])
 stock = int(i[3])
# print(tid, name, price, stock)
 q = "insert into ai17_items values('%d', '%s', '%d', '%d');"%(tid, name, price, stock)

 cur_o.execute(q)
 con_o.commit()
 print('{} row inserted'.format(i))

