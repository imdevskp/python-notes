n=input('Enter number: ')
n=int(n)

def fact(n):
 if(n==1):
  return n
 else:
  return n*fact(n-1)

print('The factorial of ' +  str(n) + ' is '+ str(fact(n)))

