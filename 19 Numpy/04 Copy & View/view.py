import numpy as np

arr = np.array([10,20,30,40])
viewedarray = arr.view()
arr[0] = 100
viewedarray[1] = 200
print(arr)
print(viewedarray)
print(viewedarray.base)
