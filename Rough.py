# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import numpy as np

#%%
array=np.array([[[1,2,3],
                 [2,4,6]],
                [[3,8,9],
                 [9,1,2]]])
print(array)
print("")
print(array[0])
print(array[0,1:])


# array[0][1]


#%%
data = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2], [-12, -4], [3, 4]])
# data
names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
names
names=="Bob"
print(data[names=="Bob"])
print(data[names=="Bob",1:])

#%%
arr = np.array([[0, 1, 0], [1, 2, -2], [6, 3, 2], [-1, 0, -1], [1, 0, 1]])
# print(arr[:])
# arr.T
n_arr=np.zeros(5,int)
for i in range(arr.shape[-1]):
    n_arr+=np.array(arr[:,i])
n_arr

#%%
arr = np.array([[0, 1, 0], [1, 2, -2], [6, 3, 2], [-1, 0, -1], [1, 0, 1]])
# arr.swapaxes(1,0)
print(list(zip(*arr)))