import numpy as np

a = np.array([[3.00, 3.20], [3.50, 3.60]])
b = np.array([118.40, 135.20])

print('A')
print(a)

print('B')
print(b)

a_inv = np.linalg.inv(a)
print('Inverse of A')
print(a_inv)

print('Count of Children and Adults')
print(np.dot(a_inv, b))
