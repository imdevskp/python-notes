class Vector():
 def __init__(self, x, y):
  self.x = x
  self.y = y

 def __str__(self):
  return self.x, self.y

 def __add__(self, other):
  return self.x+other.x, self.y+other.y

 def __eq__(self, other):
  return self.x==other.x and self.y==other.y  

v1 = Vector(1,2)
v2 = Vector(3,4)
v3 = Vector(1,2)

print('vector one is {}+{}i'.format(v1.x, v1.y))
print('vector two is {}+{}i'.format(v2.x, v2.y))
print('vector three is {}+{}i'.format(v3.x, v3.y))

print('sum of vector one and two is {}'.format(v1+v2))
print('are vector one and two equal : {}'.format(v1==v2))
print('are vector one and three equal : {}'.format(v1==v3))
