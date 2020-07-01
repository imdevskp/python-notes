import re
inp = open('emp.csv', 'r').readlines()

open('emp2.csv', 'w').write(inp[0])
oup = open('emp2.csv', 'a')

for i in inp:
    if(re.search(r'[A-Za-z\. ]*,2', i)):
        oup.write(i)
