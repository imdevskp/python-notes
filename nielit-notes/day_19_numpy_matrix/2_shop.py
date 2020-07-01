import numpy as np

print('Sales per day for each brand')
cnt = np.array([[1,5,2,3], [5,6,3,1], [7,6,2,1]])
print(cnt)

print('Price per each brand')
price = np.array([30000, 35000, 40000])
print(price)


print('Total per each day')
print(np.dot(price, cnt))
