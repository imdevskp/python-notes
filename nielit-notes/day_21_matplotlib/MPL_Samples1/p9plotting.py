#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(6,4),facecolor='#00FF00')
spobj=fobj.add_subplot(111,facecolor='0.5')
an=np.random.randint(1,100,10)
spobj.plot(an)
print(an)
plt.show()
