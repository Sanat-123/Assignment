print('1st question')
import pandas as pd

df = pd.DataFrame({
    'email': ['user@example.com', 'bademail@', 'test@domain.org'],
    'mobile': ['9876543210', '1234567890', '9999999999'],
    'name': ['Sanat', 'Vipul', 'Sachin'],
    'username': ['abc123', 'user$', 'Test456'],
    'date': ['27-06-2025', '31-02-2023', '12-12-2020']
})

df['valid_email'] = df['email'].str.match(r'.+@.+\..+')
df['valid_mobile'] = df['mobile'].str.match(r'^[6-9]\d{9}$')
df['only_alpha'] = df['name'].str.match(r'^[a-zA-Z]+$')
df['is_alnum'] = df['username'].str.match(r'^[a-zA-Z0-9]+$')
df['valid_date'] = df['date'].str.match(r'^\d{2}-\d{2}-\d{4}$')

print(df)



print('2nd question')
import pandas as pd

df = pd.DataFrame({'date': ['2025-06-25', '2024-12-01', '2023-01-15']})
df['date'] = pd.to_datetime(df['date'])

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.day_name()
df['days_diff'] = (pd.to_datetime('today') - df['date']).dt.days
df['next_week'] = df['date'] + pd.Timedelta(days=7)

print(df)


print('3rd question')
import pandas as pd

df = pd.read_csv("Customer.csv")
df = df.dropna()
df['Date'] = pd.to_datetime(df['Date'])
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
df = df[df['Amount'] > 0]

print(df['Amount'].sum())
print(df.groupby(df['Date'].dt.month_name())['Amount'].mean())
print(df['Product'].value_counts().head(1))

