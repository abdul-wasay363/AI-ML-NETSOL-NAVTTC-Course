import pandas as pd

# 1. load and tell pandas the 'date' column is a DATE, not text
df = pd.read_csv('shop_sales_daily.csv', parse_dates=['date'])
print(df.head(3))
print('From', df['date'].min().date(), 'to',df['date'].max().date(),
      '|', len(df), 'days')

# 2. pull usefull parts out of each date
df['dayofweek'] = df['date'].dt.dayofweek            # 0 = Monday ... 6 = Sunday
df['month'] = df['date'].dt.month

# 3. look for patterns
print('\nAverage sales by day of week:')
print(df.groupby('dayofweek')['sales'].mean().round())
print('\nAverage sales by years:')
print(df.groupby(df['date'].dt.year)['sales'].mean().round())