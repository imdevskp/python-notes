import MySQLdb as my

con_o = my.connect('localhost', 'ai', 'ai', 'ai')
cur_o = con_o.cursor()

f = open('sales.csv', 'r')
cont = f.readlines()
print(cont)

for row in cont[1:]:
 i = row.split(',')
 print(i)
 tid = int(i[0])
 region = i[1]
 sales = int(i[2])

 q = "insert into ai17_sales values('%d', '%s', '%d');"%(tid, region, sales)

 cur_o.execute(q)
 con_o.commit()
 print('{} row inserted'.format(i))


