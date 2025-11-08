import numpy as np

#numpy functions

arr_1d = np.arange(1,13)
print(arr_1d)

arr_2d = arr_1d.reshape(2,6)
print(arr_2d)

arr_3d = arr_1d.reshape(2,3,2)
print(arr_3d)

print(arr_2d.flatten())

print(arr_2d.transpose())

print(arr_2d.max())

print(arr_2d.max(axis= 1))
print(arr_2d.max(axis= 0))

np.sum(arr_2d, axis=0)
np.mean(arr_1d)
np.sqrt(arr_1d)
np.std(arr_2d)
np.exp(arr_1d)
np.log(arr_2d)
np.log10(arr_2d)