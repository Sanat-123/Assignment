import pandas as pd
print('1st question')
dates = ['2025-01-01', '2025-01-02', '2025-01-03']
time_series = pd.to_datetime(dates)
print("1. Time Series:")
print(time_series)
print()


print('2nd question')
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Age': [25, 30, 22]
})

print("2a. Inner Merge:")
print(pd.merge(df1, df2, on='ID', how='inner'))
print()

print("2b. Left Join:")
print(pd.merge(df1, df2, on='ID', how='left'))
print()

print("2c. Right Join:")
print(pd.merge(df1, df2, on='ID', how='right'))
print()

df1_indexed = df1.set_index('ID')
df2_indexed = df2.set_index('ID')

print("2d. Index-Based Join:")
print(df1_indexed.join(df2_indexed, how='inner'))
print()


print('3rd question')
data1 = pd.DataFrame({'ID': [1, 2], 'Score': [80, 85]})
data2 = pd.DataFrame({'ID': [3, 4], 'Score': [75, 90]})
data3 = pd.DataFrame({'ID': [1, 2, 3, 4], 'Grade': ['B', 'B+', 'C', 'A']})

combined = pd.concat([data1, data2])
print("3a. Combined Data:")
print(combined)
print()

final_result = pd.merge(combined, data3, on='ID')
print("3b. Final Merged with Grades:")
print(final_result)
print()