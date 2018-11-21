import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime as dt

fig, ax = plt.subplots()
data = pd.read_csv('../datasets/comRede.csv')
dates = data['dateTime']

initialTimeStamp = dt.datetime.strptime(dates[0],'%Y-%m-%d %H:%M:%S').timestamp()
x = [(dt.datetime.strptime(d,'%Y-%m-%d %H:%M:%S').timestamp() - initialTimeStamp)/60 for d in dates]
y = data['percentage']

ax.plot(x, y)

#Define labels
fig.suptitle('Battery benchmark', fontsize=20)
plt.xlabel('Elapsed time (minutes)', fontsize=10)
plt.ylabel('Remaining battery (%)', fontsize=10)

maxX = int(x[len(x)-1])

#Define axis limits
plt.xlim([0, maxX])
plt.ylim(0, 100)

#Custom x tickers
xTickers = []
for t in range(0, maxX, 60):
    xTickers += [t]
xTickers += [maxX]
ax.set_xticks(xTickers)

text = 'Total duration: ' + '{:02d}:{:02d}'.format(*divmod(maxX, 60))

plt.gca().annotate(text,
            fontsize=9,
            fontweight='demi',
            xy=(0, 0),  
            xycoords='data',
            xytext=(10, 20),      
            textcoords='offset points',
            bbox=dict(boxstyle="round4, pad=0.6", fc="gray", ec="b", lw=.5)) 

plt.subplots_adjust(bottom=0.5)
plt.show()