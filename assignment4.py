#question 3rd
print('3rd question')
import sqlite3

conn = sqlite3.connect("mydata.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    phone TEXT,
    address TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
)
''')

cursor.execute("INSERT INTO users (name, email) VALUES ('Sanat', 'Sanat@example.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Sachin', 'Sachin@example.com')")

cursor.execute("INSERT INTO contacts (user_id, phone, address) VALUES (1, '1234567890', 'New York')")
cursor.execute("INSERT INTO contacts (user_id, phone, address) VALUES (2, '9876543210', 'London')")


print("All Users:")
for row in cursor.execute("SELECT * FROM users"):
    print(row)

print("\nAll Contacts:")
for row in cursor.execute("SELECT * FROM contacts"):
    print(row)

print("\nUsers with Contacts:")
for row in cursor.execute("""
SELECT users.name, users.email, contacts.phone, contacts.address 
FROM users JOIN contacts ON users.user_id = contacts.user_id
"""):
    print(row)

cursor.execute("UPDATE users SET email = 'Sanat_new@example.com' WHERE name = 'Sanat'")

cursor.execute("DELETE FROM contacts WHERE contact_id = 2")

conn.commit()
conn.close()
# question 1
print('1st question')
import csv
from os import write

data =[ ["Name", "Address", "Mobile", "Email "],
        ["sachin","agra road","123","abs@gmail"],
        ["vipul", "jatapura", "605", "vip99@gmail"]
      ]
with open("data.csv","w",newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
# question 2
print('2nd question')
import requests


def weather_details(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"]
        country = data["sys"]["country"]

        print(f" Weather Details in {city}, {country}")
        print(f"Temperature     : {temperature} °C")
        print(f"Feels Like      : {feels_like} °C")
        print(f"Humidity        : {humidity}%")
        print(f"Pressure        : {pressure} hPa")
        print(f"Wind Speed      : {wind_speed} m/s")
        print(f"Description     : {description}")


    except requests.exceptions.RequestException as e:
        print(f" Error fetching data: {e}")
    except KeyError:
        print(" Some data is missing in the response. Please check the city name or try again.")


city = input("Enter the city name: ")
api_key = "a9c05b58a9f0be9c1b9a4a54b73be893"
weather_details(city, api_key)