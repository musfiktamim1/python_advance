import numpy as np

arr_1d = np.array([1,2,3,4,5])
print(arr_1d.shape) #5 columns

arr_2d = np.array([[3,4,5],[6,7,8]])
print(arr_2d.shape) # 2 rows and 3 columns

arr_nd = np.array([[[1,2,3,4,5],[6,7,8,9,10]]],ndmin=5)
print(arr_nd.shape)