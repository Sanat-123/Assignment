import numpy as np

rand_arr = np.random.rand(4, 2)
empty_arr = np.empty((4, 2))
full_arr = np.full((4, 2), 7)
zeros_arr = np.zeros((3, 5))
ones_arr = np.ones((4, 3, 2))
print(rand_arr)
print(empty_arr)
print(full_arr)
print(zeros_arr)
print(ones_arr)

matrix_3x3 = np.arange(2, 11).reshape(3, 3)
print(matrix_3x3)

null_vec = np.zeros(10)
null_vec[5] = 11
print(null_vec)

arr = np.array([1, 2, 3, 4, 5])
reversed_arr = arr[::-1]
print(reversed_arr)

int_arr = np.array([1, 2, 3, 4])
float_arr = int_arr.astype(float)
print(float_arr)