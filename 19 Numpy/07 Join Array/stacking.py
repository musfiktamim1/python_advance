import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

#horizontal stacking
arr = np.hstack((arr1,arr2))
print(arr)

#verticle stacking
arr = np.vstack((arr1,arr2))
print(arr)


#height and depth
arr = np.dstack((arr1,arr2))
print(arr)