class Vector():
 def __init__(self, x, y):
  self.x = x
  self.y = y
 def __str__(self):
  return self.x, self.y
 def __add__(self, other):
  return self.x+other.x, self.y+other.y

v1 = Vector(1,2)
v2 = Vector(3,4)

print(v1.x, v1.y)
print(v2.x, v2.y)

print(v1+v2)
