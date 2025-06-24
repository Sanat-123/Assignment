print("1st question")
name = input("Student Name: ")
student_class = input("Class: ")
print("Enter marks for 5 subjects:")
m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))
m4 = float(input("Subject 4: "))
m5 = float(input("Subject 5: "))
total = m1+m2+m3+m4+m5
percentage = total/5
print("Result")
print("Name       :", name)
print("Class      :", student_class)
print("Percentage :", round(percentage, 2), "%")





print("2nd question")
first = input("Enter first string: ")
second = input("Enter second string: ")
c = first + second
print("Combined string:", c)
print("String Operations")
print("In UPPERCASE     :", c.upper())
print("In lowercase     :", c.lower())
print("In Title Case    :", c.title())
print("Without spaces around:", c.strip())
print("Replace 'a' with '*' :", c.replace('a', '*'))
print("Position of 'is'     :", c.find('is'))
print("Total length         :", len(c))