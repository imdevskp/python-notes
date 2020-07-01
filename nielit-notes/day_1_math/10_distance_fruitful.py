#!/opt/anaconda2/bin/python
x1, y1, x2, y2 = 1,1,1,10
def distance(x1, y1, x2, y2):
 return((((x1-x2)**2)+((y1-y2)**2))**(0.5))
print(distance(1,1,1,10))