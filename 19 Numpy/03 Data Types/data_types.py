import numpy as np

"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

arr = np.array([1,2,3,4,5])
print(arr.dtype)

arr = np.array(["Apple","Banana","Cherry"])
print(arr.dtype)

"""define array dtype """

arr = np.array([1,2,3,4],dtype="S")
print(arr)
print(arr.dtype)

#as a 4byte int
arr = np.array([1,2,3,4],dtype="i4")
print(arr)
print(arr.dtype)

#converting datatype on existing array
arr = np.array([1.1,1.2,1.3,1.5])
newarr = arr.astype("i")
newarr1 = arr.astype(float)
print(arr)
print(newarr)
print(newarr1)
print(arr.dtype)
print(newarr.dtype)
print(newarr1.dtype)