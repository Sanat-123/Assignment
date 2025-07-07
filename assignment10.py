import numpy as np
import matplotlib.pyplot as plt

arr1 = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
arr1 = np.nan_to_num(arr1, nan=0)
arr1 = arr1[:, :3][:, ::-1]
print("Modified Array 1:\n", arr1)

arr3d = np.random.rand(2, 3, 4)
moved = np.moveaxis(arr3d, 0, -1)
print("Moved 3D array shape:", moved.shape)

arr_nan = np.array([[1, np.nan, 3], [4, 5, np.nan], [np.nan, 8, 9]])
col_mean = np.nanmean(arr_nan, axis=0)
inds = np.where(np.isnan(arr_nan))
arr_nan[inds] = np.take(col_mean, inds[1])
print("NaN replaced with column mean:\n", arr_nan)

arr_neg = np.array([[-2, 3], [4, -5]])
arr_neg = np.where(arr_neg < 0, 0, arr_neg)
print("Replaced negatives:\n", arr_neg)

arr1d_1 = np.array([3, 4])
arr1d_2 = np.array([1, 0])
avg = (arr1d_1 + arr1d_2) / 2
print("Average of 1D arrays:\n", avg)

arr2d_1 = np.array([[1, 2], [3, 4]])
arr2d_2 = np.array([[5, 6], [7, 8]])
combined = np.concatenate((arr2d_1, arr2d_2), axis=0)
print("Mean:", np.mean(combined))
print("Median:", np.median(combined))
print("Mode:", stats.mode(combined, axis=None).mode[0])
print("Average:\n", (arr2d_1 + arr2d_2) / 2)

A = np.array([[1, -2, 3], [-1, 3, -1], [2, -5, 5]])
B = np.array([9, -6, 17])
solution = np.linalg.inv(A).dot(B)
print("Solution of equations:", solution)

sem1 = [65, 70, 75, 80, 68]
sem2 = [75, 72, 78, 85, 70]
subjects = ['Math', 'Sci', 'Eng', 'CS', 'Hist']

plt.plot(subjects, sem1, marker='o', label='Sem 1')
plt.plot(subjects, sem2, marker='s', label='Sem 2')
plt.title("Semester Result Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()
