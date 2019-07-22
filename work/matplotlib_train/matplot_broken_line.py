import matplotlib.pyplot as plt
import random
plt.figure()
x1 = list(range(10))
y1 = [random.randint(0, 10) for i in range(10)]
plt.plot(x1, y1, color='r', markerfacecolor='blue', marker='o')
# for a, b in zip(x1, y1):
#     plt.text(a, b, "app-({0},{1})".format(a,b), ha='center', va='bottom', fontsize=10)

plt.show()
