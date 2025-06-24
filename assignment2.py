print('question 1st')
name = input("Enter Student Name: ")
student_class = input("Enter Class: ")

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

if percentage >= 60:
    grade = 'A'
elif percentage >= 50:
    grade = 'B'
elif percentage >= 40:
    grade = 'C'
elif percentage >= 33:
    grade = 'D'
else:
    grade = 'Fail'

print("Student Report")
print("Name       :", name)
print("Class      :", student_class)
print("Total      :", total)
print("Percentage :", round(percentage, 2), "%")
print("Grade      :", grade)





print('2nd question')
num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")





print('3rd question')
items = []
prices = []

while True:
    print("\n1. Add Items\n2. Show Bill\n3. Show Total\n4. Exit")
    choice = input("Choose (1-4): ")

    if choice == '1':
        for _ in range(int(input("How many items? "))):
            items.append(input("Item name: "))
            prices.append(float(input("Price: ₹")))
    elif choice == '2':
        if items:
            total = 0
            for i in range(len(items)):
                print(f"{items[i]} - ₹{prices[i]}")
                total += prices[i]
            print("Total: ₹", total)
        else:
            print("No items added yet.")
    elif choice == '3':
        print("Total: ₹", sum(prices))
    elif choice == '4':
        break
    else:
        print("Invalid option.")




print('4th question')
numbers = [10, 5, 8, 20, 3, 5]

unique = sorted(set(numbers))

print("Original List:", numbers)
print("Smallest number       :", unique[0])
print("Second smallest number:", unique[1])
print("Second greatest number:", unique[-2])
