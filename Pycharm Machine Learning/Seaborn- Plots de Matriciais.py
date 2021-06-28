import matplotlib.pyplot as plt
import seaborn as sns

flights = sns.load_dataset('flights')
tips = sns.load_dataset('tips')

print(tips.corr())

'''sns.heatmap(tips.corr(), cmap='coolwarm', annot=True) # heatmat is map of warmth'''

flights.pivot_table(values='passengers',index='month',columns='year')

pvflights = flights.pivot_table(values='passengers',index='month',columns='year')
sns.heatmap(pvflights)

'''sns.heatmap(pvflights,cmap='magma',linecolor='white',linewidths=1)'''

sns.clustermap(pvflights, standard_scale=1)

plt.show()
