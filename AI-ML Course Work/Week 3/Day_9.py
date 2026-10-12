import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
print(df.shape)
print(df.head())
print(df.dtypes)

df = sns.load_dataset('tips')
print(df.shape)
print(df.head())
print(df.dtypes)

df = sns.load_dataset('tips')


print(df.describe())


# unvariets: counts catagories

df = sns.load_dataset('tips')
print(df['day'].value_counts())

print(df[['sex', 'time']].value_counts())

df = sns.load_dataset('tips')
sns.histplot(df['total_bill'])
plt.show()

df = sns.load_dataset('tips')
print(df.groupby('day')['total_bill'].mean())

df = sns.load_dataset('tips')
df.plot(x='total_bill', y='tip', kind='scatter')  # by using pandas 
plt.show()

df = sns.load_dataset('tips')
sns.scatterplot(x='total_bill', y='tip', data = df)  # by using Seaborn
plt.show()

df = sns.load_dataset('tips')
correlation = df[['total_bill','tip','size']].corr()
print(correlation)
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.show()