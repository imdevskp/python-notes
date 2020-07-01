import re

f = open('emp.csv').readlines()

sc_ls = []
sc_ls.append(f[0])

for i in f[1:]:
 if re.search('scientist', i):
  sc_ls.append(i)

st  = ''
for i in sc_ls:
 st += i

f = open('sci.csv','w').write(st)
