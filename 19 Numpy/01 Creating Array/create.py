import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

"0-d array"
arr1 = np.array(42)
print(arr1)

"1-d array"

arr_1d = np.array([1,2,3,4,5])
print(arr_1d)

"2-d array"

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d)

"3-d array"
arr_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr_3d)


"check number of dimensions"
d_0 = np.array(10)
d_1 = np.array([10,20,30,40])
d_2 = np.array([[10,20],[30,40]])
d_3 = np.array([[[10,20],[30,40]],[[50,60],[70,80]]])

print(d_0.ndim)
print(d_1.ndim)
print(d_2.ndim)
print(d_3.ndim)

"higher dimensional array"

d_h = np.array([1,2,3,4,5],ndmin=5)
print(d_h)
print(d_h.ndim)