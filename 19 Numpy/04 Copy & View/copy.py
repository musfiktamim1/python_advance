import numpy as np

arr = np.array([10,20,30,40])
copiedarray = arr.copy()
arr[0] = 100
print(arr)
print(copiedarray)
print(copiedarray.base)
