import numpy as np

a = np.array([1, 2, 3])
b = np.array([[4, 5, 6]])
combined = np.vstack((a, b))
print("Combined Array:\n", combined)

arr2d = np.array([[1, 2], [3, 4]])
flattened = arr2d.flatten()
print("Flattened Array:", flattened)

reversed_arr = arr2d[::-1]
print("Reversed Array:\n", reversed_arr)

arr = np.array([[10, 5, 8], [2, 15, 3]])
max_val = np.max(arr)
print("Max Value:", max_val)

min_val = np.min(arr)
print("Min Value:", min_val)

shape = arr.shape
rows = shape[0]
cols = shape[1]
print("Rows:", rows, "Cols:", cols)

all_elements = arr[:]
print("All Elements:\n", all_elements)

specific_element = arr[1, 2]
print("Specific Element [1,2]:", specific_element)

total = 0
for i in range(rows):
    for j in range(cols):
        total += arr[i, j]
print("Sum using loop:", total)

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
