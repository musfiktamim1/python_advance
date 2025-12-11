# Iterating means going through elements one by one.

import numpy as np

arr = np.array([1,2,3,4])

for x in arr:
    print(x)


"2d iterating"
arr = np.array([[1,2],[3,4]])
for x in arr:
    print(x)

for x in arr:
    for y in x:
        print(y)


"2d iterating"
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for x in arr:
    print(x)

for x in arr:
    for y in x:
        print(y)
for x in arr:
    for y in x:
        for z in y:
            print(z)

#iterating each scalar element

arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

for x in np.nditer(arr):
    print(x)

for ind,x in np.ndenumerate(arr):
    print(ind,x)