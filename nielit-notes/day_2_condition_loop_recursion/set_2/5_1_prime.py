n=input('Enter number: ')
n=int(n)
isPrime = True

for i in range(2, (n/2)):
 if n%i==0:
  isPrime=False

print(isPrime)  

