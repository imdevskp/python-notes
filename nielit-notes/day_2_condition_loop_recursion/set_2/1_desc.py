n=input("Enter the starting number: ")

def decrease(n):
 if(n!=0):
  print(n)
  decrease(n-1)

decrease(n)
