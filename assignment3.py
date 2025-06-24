print('1st question')
student = {"name": "Alex", "age": 20, "grade": "A"}
print("Dictionary Example:", student)

fruits = ("apple", "banana", "cherry")
print("Tuple Example:", fruits)

unique_numbers = {1, 2, 3, 2, 4, 1}
print("Set Example (no duplicates):", unique_numbers)


print('2nd question')
def basic_operations(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: Cannot divide by zero")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

basic_operations(num1, num2)

print('3rd question')
def is_palindrome(number):
    original = str(number)
    reversed_num = original[::-1]
    if original == reversed_num:
        print(f"{number} is a Palindrome Number")
    else:
        print(f"{number} is NOT a Palindrome Number")

num = input("Enter a number to check for palindrome: ")
is_palindrome(num)
