print("1st question")
import pandas as pd

marks = pd.Series({'Math': 90, 'Science': 85, 'English': 92})
print(marks['Science'])

colleges = pd.Series(['SKIT', 'Poornima', 'JECRC'], index=['a', 'b', 'c'])
print(colleges['a'])


print('2nd question')
data1 = [[1, 'Sumit'], [2, 'Yash']]
df1 = pd.DataFrame(data1, columns=['ID', 'Name'])
print(df1)

data2 = {'Name': ['Sanat', 'Sachin'], 'Age': [25, 30]}
df2 = pd.DataFrame(data2)
print(df2)

data3 = [(101, 'Red'), (102, 'Blue')]
df3 = pd.DataFrame(data3, columns=['Code', 'Color'])
print(df3)

data4 = [{'Product': 'Pen', 'Price': 10}, {'Product': 'Pencil', 'Price': 5}]
df4 = pd.DataFrame(data4)
print(df4)


print('3rd question')
df = pd.DataFrame({
    'Name': ['Sanat', 'Vipul', 'Sachin'],
    'Score': [88, 76, 93]
})

for i, row in df.iterrows():
    print(f"{row['Name']} scored {row['Score']}")

high_scores = df[df['Score'] > 80]
print(high_scores)

print(df.iloc[1])

print(df[['Name']].head(2))

df_new = df[df['Name'] != 'Sanat']
print(df_new)

df.loc[1] = ['Sanat', 89]
print(df)

new_students = [{'Name': 'Vipul', 'Score': 95}, {'Name': 'Sachin', 'Score': 82}]
df2 = pd.DataFrame(new_students)
print(df2)