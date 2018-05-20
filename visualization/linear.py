import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 50)
y = x ** 2
y2 = x ** 3

plt.plot(x, y, '.-',label='x ** 2', lw=1)
plt.plot(x, y2, '--', label='x ** 3', color='red')
plt.legend(loc=0)
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('Graph Title Here')
plt.show()
# plt.savefig('myfig') Save the plot

# Another way to do that
# fig = plt.figure()
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes.plot(x, y, 'b')
# axes.set_xlabel('Set X Label')
# axes.set_ylabel('Set y Label')
# axes.set_title('Set Title')
# plt.show()