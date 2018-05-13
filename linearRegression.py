import seaborn as sns
import matplotlib.pylab as plt

tips = sns.load_dataset("tips")

sns.lmplot(x="total_bill", y="tip", hue="sex",
 data=tips, markers=["o", "o"], legend_out = False)
plt.show()