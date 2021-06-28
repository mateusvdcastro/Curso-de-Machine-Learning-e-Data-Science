from modules import line, título
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

título('Pandas')
df1 = pd.read_csv('Ecommerce Purchases.csv')
print(df1.head())
print(df1.columns)
print(df1['Email'].apply(lambda x: x.split('@')[-1]).value_counts().head(5))

line(50)

título('Matplotlib')
x = np.linspace(0, 5, 11)
y = x**2
plt.plot(x, y, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Função exponêncial')
plt.show()

line(50)




