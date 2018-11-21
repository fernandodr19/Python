import pandas as pd
import seaborn as sns

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as matdates
import matplotlib.ticker as ticker


import datetime as dt

fig, ax = plt.subplots()
N = 100
data = pd.read_csv('../datasets/teste.csv')
dates = data['dateTime']

initialTimeStamp = dt.datetime.strptime(dates[0],'%Y-%m-%d %H:%M:%S').timestamp()
x = [dt.datetime.strptime(d,'%Y-%m-%d %H:%M:%S').timestamp() - initialTimeStamp for d in dates]
y = data['battery']

ax.plot(x, y)

fig.suptitle('Battery benchmark', fontsize=20)
plt.xlabel('Elapsed time (s)', fontsize=10)
plt.ylabel('Remaining battery (%)', fontsize=10)


plt.xlim([x[0], x[len(x) - 1]])
plt.ylim([y[len(y) - 1], y[0]])

ax.yaxis.set_major_locator(ticker.MultipleLocator(base=1.0))

plt.subplots_adjust(bottom=0.5)
plt.show()