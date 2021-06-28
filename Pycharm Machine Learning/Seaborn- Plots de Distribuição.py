import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# fig 1
sns.set_theme(style='white')
mpg = sns.load_dataset('mpg')
sns.relplot(x="horsepower", y="mpg", hue="origin", size="weight",
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=mpg)

# fig 2
tips = sns.load_dataset('tips')

sns.displot(tips['total_bill'], kde=False, bins=30) # kde = tira a linha de progressão; bins = deixa as barras menos retângulares
# fig 3
sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
# fig 4
sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')
# fig 5
sns.pairplot(tips, hue='sex', palette='coolwarm')
# fig 5 último bloco
sns.kdeplot(tips['tip'])
sns.rugplot(tips['tip'])



plt.show()
