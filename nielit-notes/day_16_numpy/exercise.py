# 1. open a python interpreter

# 2. import numpy
import numpy as np

# 3. create a 1D array having 5 elements (integers) using array method
ar1 = np.array([1, 2, 3, 4, 5])
print(ar1)

# 4. do 3 using arange  	
ar2 = np.arange(1,6)
print(ar2)
 
# 5. create a 3 dimensional array containing 1s(integers), there should be 40 members
ar3 = np.arange(1,41).reshape(2,4,5)
print(ar3)

# 6. print the total number of elements (size) for the above array
print(ar3.size)

# 7. Check and explain the difference between array and asarray
ar_x = np.array([1,2,3,4])
ar_y = np.asarray(ar_x)
ar_z = ar_x
print(ar_x)
print(ar_y)
print(ar_z)
print(ar_x is ar_y)
print(ar_x is ar_z)
ar_x[1]=8
print(ar_x)
print(ar_y)
print(ar_z)

# 8. Create an identity mtrix of a given specification.
ar8 = np.identity(4)
print(ar8)

# 9. Create an array containing 0s inheriting shape from the array created in Q.No.5
s = ar3.shape
ar9 = np.zeros(s)
print(ar9)

# 10.Print the size,shape,dimensions and datatype of all the above arrays. 
print('ar1')
print(ar1)
print(ar1.size)
print(ar1.shape)
print(ar1.ndim)
print(ar1.dtype)	
print('-'*18)

print('ar2')
print(ar2)
print(ar2.size)
print(ar2.shape)
print(ar2.ndim)
print(ar2.dtype)	
print('-'*18)


print('ar3')
print(ar3)
print(ar3.size)
print(ar3.shape)
print(ar3.ndim)
print(ar3.dtype)	
print('-'*18)


print('ar8')
print(ar8)
print(ar8.size)
print(ar8.shape)
print(ar8.ndim)
print(ar8.dtype)	
print('-'*18)


print('ar9')
print(ar9)
print(ar9.size)
print(ar9.shape)
print(ar9.ndim)
print(ar9.dtype)	
print('-'*18)
