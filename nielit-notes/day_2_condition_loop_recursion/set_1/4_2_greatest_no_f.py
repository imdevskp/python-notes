n1, n2, n3 = 5, 4, 9

def greatest_no():
 if(n1>n2):
  greatest=n1
 else:
  greatest=n2
 if(n3>greatest):
  greatest=n3
 return greatest

print greatest_no()
