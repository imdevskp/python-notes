s = raw_input('Please enter the sentence : ')
s = s.split()

d = {}

for wd in s:
 if wd in d:
  d[wd] += 1
 else:
  d[wd] = 1

print(d)
