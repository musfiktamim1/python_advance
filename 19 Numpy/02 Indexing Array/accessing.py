import numpy as np

"""
1_d 

d_1 = np.array([10,20,30,40])
print(d_1)
print(d_1[1])
print(d_1[0])
print(d_1[-1])
print(d_1[0]+d_1[2])
print(d_1[2:3])
print(d_1[:3])
print(d_1[2:])
print(d_1[:])
print(d_1[::-1])
print(d_1[::2])

"""
"""
2_d

d_2 = np.array([[10,20],[30,40]])
print(d_2)
print(d_2[0,1])
print(d_2[0,0])
print(d_2[1,0])
print(d_2[1,1])
print(d_2[-1,-1])
print(d_2[:,1])
print(d_2[:,0])
print(d_2[:,:])
print(d_2[::-1,::-1])
"""

d_3 = np.array([[[10,20],[30,40]],[[50,60],[70,80]]])
print(d_3)
print(d_3[0,0,0])
print(d_3[0,0,1])
print(d_3[0,1,0])
print(d_3[0,1,1])

print(d_3[1,0,0])
print(d_3[1,0,1])
print(d_3[1,1,0])
print(d_3[1,1,1])

print(d_3[:,:,1])
print(d_3[:,:,0])
print(d_3[::-1,::-1,::-1])