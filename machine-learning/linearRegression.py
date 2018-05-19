import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

USAhousing = pd.read_csv('../datasets/USA_Housing.csv')

# sns.despine() # remove top and right ticks
# sns.set_style("darkgrid")
# sns.distplot(USAhousing['Price']) # avg = 1.000.000
# plt.show()

X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]

y = USAhousing['Price'] # target

# split my data into train and test
# test_size -> percent of data alocated to test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

#instanciate the model
lm = LinearRegression()

# train the model
lm.fit(X_train,y_train)

# coefficient of each attr
# Holding all other features fixed, a 1 unit increase in Avg. Area Income is 
# associated with an increase of $21.52 .
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
# print(coeff_df)

### Predictions
predictions = lm.predict(X_test) #y_test contains the right values

plt.scatter(y_test,predictions)
plt.xlabel('Y test (true values)')
plt.ylabel('Predictions')
# plt.show()

print(X_test.iloc[0])
print(y_test.iloc[0])
X_predict = X_test.iloc[0].values.reshape(1,-1)
y_predict = lm.predict(X_predict)
print(y_predict[0]) #very close to y_test.iloc[0]

