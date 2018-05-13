import numpy as np
import matplotlib.pyplot as plt
 
objects = ('Label1', 'Label2', 'Label3', 'Label4', 'Label5', 'Label6')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,7,1]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Y axis')
plt.title('Title')
 
plt.show()