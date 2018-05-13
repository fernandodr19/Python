import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

df = pd.read_csv('datasets/911.csv')

# Create reason col
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])

# Convert time stamp from str to datetime
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# Create extra cols
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
dmap = {i: day for i, day in enumerate(days)}
df['Day of Week'] = df['Day of Week'].map(dmap)

sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis',order=days)
plt.show()