import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)
print("\n")
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)
print("\n")
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
range_arr = np.arange(0, 10, 2)   # start, stop, step
linspace_arr = np.linspace(0, 1, 5)  # 5 evenly spaced values between 0 and 1

print(zeros)
print("\n")
print(ones)
print("\n")
print(range_arr)
print("\n")
print(linspace_arr)

print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Size:", arr2.size)
print("Data type:", arr2.dtype)

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])       # first element
print(arr[-1])      # last element
print(arr[1:4])     # slice
print("\n")

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[1, 2])     # row 1, col 2 → 6
print(matrix[:, 1])     # all rows, column 1
print(matrix[0:2, 0:2]) # sub-matrix

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
print("\n")

print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Max:", np.max(a))
print("Min:", np.min(a))
print("Standard Deviation:", np.std(a))
print("\n"*20)
# Program: Calculate statistics of student marks
marks = np.array([85, 90, 78, 92, 88, 76, 95])

print("Marks:", marks)
print("Average marks:", np.mean(marks))
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Marks above average:", marks[marks > np.mean(marks)])

# Program: Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = np.dot(A, B)
print("Matrix multiplication result:\n", result)