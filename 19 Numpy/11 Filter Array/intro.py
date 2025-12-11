import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, True, True, False]

newarr = arr[x]

print(newarr)

#creating filter arr
newarr = arr[arr>=43]
print(newarr)
print(newarr.base)
newarr = arr[arr%2==0]
print(newarr)