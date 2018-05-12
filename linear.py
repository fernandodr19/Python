import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 50)
y = x ** 2
y2 = x ** 3

plt.plot(x, y)
plt.plot(x, y2, 'r') # 'r' is the color red
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('Graph Title Here')
plt.show()