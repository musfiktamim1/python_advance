import numpy as np

"""1d to 2d"""
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape((4,3))
print(arr)
print(newarr)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape((2,2,3))
print(arr)
print(newarr)

print("copy or view",newarr.base) # return view

#unknown dimension
arr = np.array([1,2,3,4,5,6,7,8]) 
newarr = arr.reshape(2,2,-1)
print(newarr)

#flattening multi dimension to single dimension
arr = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
newarr = arr.flatten()
print(newarr)
print(newarr.base) #return copy

#ravel multi dimension to single dimension
arr = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
newarr = arr.ravel()
print(newarr)
print(newarr.base) #return view

