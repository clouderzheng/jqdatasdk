import matplotlib.pyplot as plt

plt.figure()
ax = plt.axes()
ax.arrow(1, 1, 1, 1, color='y', head_width=0.05, head_length=0.1, fc='k', ec='k')
plt.plot((1, 2), (1, 2), color='r', markerfacecolor='blue', marker='o')
# plt.axis("off")
plt.xlim(0,10)
plt.ylim(0,10)
plt.show()