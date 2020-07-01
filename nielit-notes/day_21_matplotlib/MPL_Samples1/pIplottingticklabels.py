#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(10,10),facecolor='#00FF00')
fobj.canvas.set_window_title('My-Figure')
fobj.suptitle('My-Plots')
spobj=fobj.add_subplot(1,1,1)
yn=np.random.randint(1,100,9)
xn=np.arange(2,20,2)
xts=np.linspace(0,20,5)
yn.sort()
spobj.plot(xn,yn,'ro:',drawstyle='steps-mid')
spobj.set_xticks(xts)
spobj.set_xticklabels(['zero','Quartile1','Half','Quartile3','Full'],rotation=90,fontsize='small')
spobj.set_xlabel('Parts')
spobj.set_title('A sample plot')
print('xn=',xn)
print('yn=',yn)
plt.show()
