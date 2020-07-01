import re

f = open('emp.csv').readlines()

sc_ls = []
sc_ls.append(f[0])

for i in f[1:]:
 if re.match('\w{1}\.', i):
  sc_ls.append(i)

st  = ''
for i in sc_ls:
 st += i

f = open('ini1.csv','w').write(st)
