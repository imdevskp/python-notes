import sys

fo, n = open(sys.argv[1], 'w+'), int(sys.argv[2])

m = [i*n for i in range(1, 11)]

sent = ''

for i in range(1, len(m)+1):
 line = str(i)+' x '+str(n)+' = '+str(i*n)
 sent = sent+line+'\n'
 
fo.write(sent)
