"""Splitting is reverse operation of Joining."""
import numpy as np
arr1 = np.array([1,2,3,4,5,6])
arr = np.array_split(arr1,3)
print(arr)
arr = np.array_split(arr1,4)
print(arr)
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])

# split 2d array
arr1 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
arr = np.array_split(arr1,3)
print(arr)

arr1 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
arr = np.array_split(arr1,3,axis=1)
print(arr)