class Complex():
 def __init__(self, x, y):
  self.x = x
  self.y = y

 def __str__(self):
  return '{}+{}i'.format(self.x, self.y)

 def __add__(self, other):
  return '{}+{}i'.format(self.x+other.x, self.y+other.y)

c1 = Complex(1,2)
c2 = Complex(3,4)

print(c1)
print(c2)

print(c1+c2)
