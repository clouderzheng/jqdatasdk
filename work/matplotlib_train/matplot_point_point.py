import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()

plt.plot((1,2), (1,2), color='r', markerfacecolor='blue', marker='o')
plt.text(0.5,1,"AbstractAutowireCapableBeanFactory",ha='center', va='bottom', fontsize=18)
plt.plot((1,2), (1,3), color='r', markerfacecolor='blue', marker='o')
# plt.xticks([])  #去掉横坐标值
# plt.yticks([])
plt.axis('off')

plt.show()