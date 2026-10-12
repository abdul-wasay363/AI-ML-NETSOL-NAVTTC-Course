import pandas as pd
import matplotlib.pyplot as plt

# Pandas and Creating DataFrame
data = {'name': ['ALi', 'Sara', 'Zain'],
        'marks': [85,92,78]}
df = pd.DataFrame(data)
print(df)

# task
data = {
    'name':['ALi', 'Sara', 'Zain','Muneeb'],
    'city':['Lahore', 'Multan', 'Faisalabad','Karachi'],
    'score':[89,75,68,91]
}
df = pd.DataFrame(data)
print(df)

# Series vs DataFrame 
s = pd.Series([10,20,30], index=['a','b','c'])
print(s)

df = pd.DataFrame({'name':['ALi', 'Sara'], 'marks':[78,96]})
print(df['name']) # a Series

# task
s_c = pd.Series(['Lahore', 'Multan', 'Faisalabad','Karachi','Islamabad'],index=['c1','c2','c3','c4','c5'])
print(s_c)
# task
_data = {
    'name':['ALi', 'Sara', 'Zain','Muneeb'],
    'city':['Lahore', 'Multan', 'Faisalabad','Karachi'],
    'score':[89,75,68,91]
}
df = pd.DataFrame(_data)
print(df['city'])
print(type(df['city']))

# Selection & Indexing
# task
df = pd.DataFrame(
    {
        'name':['ALi', 'Sara', 'Zain','Muneeb','Talha'],
        'city':['Lahore', 'Multan', 'Faisalabad','Karachi','Islamabad'],
        'score':[89,75,68,91,79]
    }
)
print(df[df['score']>75])
# task
print(df[["name", "score"]])
print(df)

# DataFrame Operations
data = {'name': ['ALi', 'Sara', 'Zain'],
        'marks': [85,92,78]}
df = pd.DataFrame(data)

df['grade'] = df['marks'].apply(
    lambda x: "Pass" if x >= 80 else "Fail"
)
print(df.sort_values("marks",ascending=False))

# task
data = {'values': [10,35,78,98,43,23,65]}
df = pd.DataFrame(data)
# task
df['Temperature'] = df['values'].apply(
    lambda x: 'High' if x >= 50 else 'Low'
)
print(df.sort_values("Temperature",ascending=False))
print(df.value_counts("Temperature"))

# Handling Missing Data
df = pd.DataFrame({'a':[1,2,None],'b':[4,None,6],'c':[7,8,9]})
print(df.isnull())
print(df.fillna(0))
df2 = pd.DataFrame({'a':[1,2,3],'b':[4,None,6],'c':[7,8,9]})
print(df2.dropna())
print(df2.isnull())

# GroupBy
sales = pd.DataFrame(
    {
        "dept": ["IT", "IT", "HR", "HR"],
        "sales": [100, 150, 80, 90]
    }
)

print(sales.groupby("dept")["sales"].sum())

# task
product = pd.DataFrame(
    {
        "catagory": ["Pizza", "Pizza", "Burger", "Burger"],
        "price": [100, 150, 80, 90]
    }
)
print(product.groupby("catagory")["price"].sum()/2)         # sum()/2 = mean()
# task
print(product.groupby("catagory")["price"].mean().count())

# Merging & Concatenation
a = pd.DataFrame({'id': [1,2,3], 'name':['ALi', 'Shoaib', 'Asghar'] })
b = pd.DataFrame({'id': [1,2,4], 'marks':[85, 95, 50] })

print(pd.merge(a, b, on='id', how = 'left'))  # how = 'outer'/'right'/'left'/'inner/...'


# task
a = pd.DataFrame({'id': [1,2,3], 'name':['ALi', 'Shoaib', 'Asghar'] })
b = pd.DataFrame({'id': [1,2,4], 'marks':[85, 95, 50] })

print(pd.merge(a, b, on='id', how = 'left')) 
print(pd.merge(a, b, on='id', how = 'inner'))
print(pd.concat([a,b])) 

# Pandas Plotting
df = pd.DataFrame({"dept": ["IT","HR","Sales"],"revenu": [250, 170, 300]})
df.plot(x='dept', y='revenu', kind="scatter")
plt.show()
