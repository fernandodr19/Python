import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Data
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [15, 30, 45, 10]

plt.pie(fracs, explode=(0, 0, 0, 0),
        labels=labels, autopct='%.0f%%',
        shadow=False, radius=1.0)

plt.show()