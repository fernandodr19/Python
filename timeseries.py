import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data = pd.read_csv('datasets/df1.csv')
sns.set_style('darkgrid')


import datetime as dt

dates = data['Date']

x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in dates]
y = data['B']

ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=5))
plt.plot(x,y)
# plt.figure(figsize=(12,3))
plt.gcf().autofmt_xdate()


bbox_props = dict(boxstyle="round4, pad=0.6", fc="cyan", ec="b", lw=.5)

maxY = y.max()
maxYIndex = y.idxmax(axis=0, skipna=True)
dateOfMaxY = data.at[maxYIndex,'Date']
formatedDate = dt.datetime.strptime(dateOfMaxY, '%Y-%m-%d').strftime('%-m/%d/%Y')

print(maxY) # max y
print(maxYIndex) # index of max y
print(formatedDate) # Date of max y

text = 'Global Max = ' + str(round(maxY, 2)) + '\nDate = ' + formatedDate

plt.gca().annotate(text,
            fontsize=9,
            fontweight='demi',
            xy=(formatedDate, maxY),  
            xycoords='data',
            xytext=(10, 20),      
            textcoords='offset points',
            arrowprops=dict(arrowstyle="->"), bbox=bbox_props) 


plt.show()