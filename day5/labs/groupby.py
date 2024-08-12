import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Values': [10, 20, 15, 25, 5, 30]
})

# Group by 'Category' and calculate the mean of 'Values'
grouped = df.groupby('Category').mean()
print("Mean")
print(grouped)

grouped = df.groupby('Category').agg({
    'Values': ['mean', 'sum', 'max', 'count']
})
print("Aggregates")
print(grouped)

# Sample DataFrame
df = pd.DataFrame({
    'Date': ['2024-08-01', '2024-08-01', '2024-08-02', '2024-08-02'],
    'Category': ['A', 'B', 'A', 'B'],
    'Values': [10, 20, 15, 25]
})

# Pivot Table
pivot_table = pd.pivot_table(df, values='Values', index='Date', columns='Category', aggfunc='sum')
print(pivot_table)






