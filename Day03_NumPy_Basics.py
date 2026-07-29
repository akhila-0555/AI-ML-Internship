
import numpy as np
print("----- Creating Arrays -----")
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([[1, 2, 3],[4, 5, 6]])
print("1D Array:")
print(arr1)
print("\n2D Array:")
print(arr2)


print("\n----- Array Information -----")
print("Dimensions:", arr2.ndim)
print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)


print("\n----- Array Indexing -----")
print("First Element:", arr1[0])
print("Last Element:", arr1[-1])
print("Element at Row 2, Column 3:", arr2[1, 2])


print("\n----- Array Slicing -----")
print("Elements from Index 1 to 3:", arr1[1:4])


print("\n----- Mathematical Operations -----")
a = np.array([10, 20, 30])
b = np.array([2, 4, 6])
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


print("\n----- Statistical Functions -----")
numbers = np.array([15, 25, 35, 45, 55])
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
print("Standard Deviation:", np.std(numbers))


print("\n----- Array-Based Calculation -----")
marks = np.array([85, 90, 78, 92, 88])
print("Student Marks:", marks)
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
percentage = (marks / 100) * 100
print("Percentage:", percentage)