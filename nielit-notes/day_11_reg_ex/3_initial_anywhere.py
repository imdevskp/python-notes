import re

f = open('emp.csv').readlines()

print(f)

sc_ls = []
sc_ls.append(f[0])

for i in f[1:]:
 if re.search('[a-zA-Z]{1}\.', i):
  sc_ls.append(i)

st  = ''
for i in sc_ls:
 st += i

print(st)

f = open('ini2.csv','w').write(st)
