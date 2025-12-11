import numpy as np

arr = np.array([1,2,3,4,5,6,4,5])
indar = np.where(arr==4)
print(indar)

indar = np.where(arr%2==0)
print(indar)

x = np.searchsorted(arr,3)
print(x)
x = np.searchsorted(arr,4) #first index of array
print(x)

x = np.searchsorted(arr,4,side="left") #first index of array
print(x)

x = np.searchsorted(arr,4,side="right") #last index of array
print(x)

x = np.searchsorted(arr,[4,5,3]) #multiple search
print(x)