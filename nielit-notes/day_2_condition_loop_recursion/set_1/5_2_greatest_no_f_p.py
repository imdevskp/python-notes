def greatest_no(n1, n2, n3):
 if(n1>n2):
  greatest=n1
 else:
  greatest=n2
 if(n3>greatest):
  greatest=n3
 return greatest

print greatest_no(3,2,1)
print greatest_no(4,6,5)
print greatest_no(1,3,9)
