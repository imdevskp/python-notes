import numpy as np

a = int(input('Please Input the starting no. : '))
b = int(input('Please Input the ending no. : '))

arr = np.arange(a, b+1)
arr.resize(4,4)
print(arr)

n = int(input('Enter the number to divide :'))
print('Divisible by {} are {}'.format(n, arr[arr%n==0]))
print('Not Divisible by {} are {}'.format(n, arr[arr%n!=0]))
