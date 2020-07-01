import re

f = open('emp.csv').readlines()

names = [] 
no = []

for i in f[1:]:
 name = re.findall('^[a-zA-Z\.\s]*', i)
 names.append(name[0])
 ph = re.findall('[\(\{\[]*\d{4}[\)\}\]]*[-_]\d{7}', i)
 ph = re.sub(r'[\-\_\(\)\[\]\{\}]', '', ''.join(ph))
 no.append(ph)

txt = ''
for i in range(len(names)):
 txt += names[i]+','+no[i]+'\n'

open('empphno.csv','w').write(txt)
