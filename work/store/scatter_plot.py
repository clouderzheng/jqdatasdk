
import matplotlib.pyplot as plt
import  numpy as np
n = 1024
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
t = np.arctan2(y,x)
# plt.scatter(np.arange(5),np.arange(5))
plt.scatter(x,y,s=75,c=t,alpha=0.5)
plt.show()
