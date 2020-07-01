n=input('Enter number: ')
n=int(n)
m=n

fact=1

while(n!=1):
 fact = fact*n
 n = n-1

print('The factorial of ' +  str(m) + ' is '+ str(fact))

