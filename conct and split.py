import numpy as np

mx1 = np.arange(1,17).reshape(4,4)
mx2 = np.arange(17,33).reshape(4,4)
print(mx1)
print(mx2)

print(np.concatenate((mx1, mx2), axis=1))

print(np.vstack((mx1,mx2)))
print(np.hstack((mx1,mx2)))

print(np.split(mx1, 2, axis=1))