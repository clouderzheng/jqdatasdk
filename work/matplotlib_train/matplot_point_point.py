import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
x = np.linspace(-10, 10, 2000)
y1 = np.sin(x)
# plt.plot(x, y1)
plt.plot((2, 0),(1,3))
plt.plot((2, 1),(1,3))
plt.plot((2, 4),(1,3))
plt.xlim((-5,5))
plt.ylim((-5,5))

#设置为坐标原点为中心
# ax.spines['bottom'].set_position('center')
# ax.spines['left'].set_position('center')

plt.show()