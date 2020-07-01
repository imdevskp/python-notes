n=input('Enter number: ')
n=int(n)
f=True

def prime(n):
 hn=n/2
 while(hn>1):
  if(n%hn==0):
   f=False
   return f
   break

f=prime(n)

print(f)
