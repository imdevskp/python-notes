import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(6,3))
ax = fig.add_subplot(111)

x = np.arange(2, 21, 2)

y = np.random.randint(1,100,10)
y.sort()
y1 = y[y<50]
y2 = y[y>=50]
y2 = np.insert(y2, 0, y1[y1.size-1])

print(x)
print(y)
print(y1)
print(y2)

ax.plot(x[:y1.size], y1, linestyle='solid', color='red')
ax.plot(x[y1.size-1:], y2, linestyle='solid', color='black')

plt.show()
