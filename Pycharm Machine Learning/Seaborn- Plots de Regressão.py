import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm',
           markers=['o','v'],scatter_kws={'s':100})

sns.lmplot(x="total_bill", y="tip", row="sex", col="time",data=tips)

plt.show()

help(sns.lmplot)
