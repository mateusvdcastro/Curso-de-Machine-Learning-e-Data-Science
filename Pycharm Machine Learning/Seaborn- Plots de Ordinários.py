import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips)
sns.violinplot(x="day", y="total_bill", data=tips, hue='sex', split=True, palette='Set1')

'''sns.boxplot(data=tips,palette='rainbow',orient='h')'''

'''sns.violinplot(x="tip", y="day", data=tips,palette='rainbow')
sns.swarmplot(x="tip", y="day", data=tips,color='black',size=3)'''

plt.show()
