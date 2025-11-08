import numpy as np
import random


print(np.random.random(1))

print(np.random.random((3,3)))

print(np.random.randint(1,4, (3,3)))

np.random.seed(10)
print(np.random.randint(1,4, (3,3)))

np.random.seed(10)
print(np.random.randint(1,4, (3,3)))

print(np.random.rand(3,3))

print(np.random.randn(3,3))

x = [1,2,3,4]

np.random.choice(x)

for i in range(20):
    print(np.random.choice(x))

str1 = "Introduction to Machine Learning"

print(np.char.center(str1, 60,fillchar="*"))

print(np.char.split(str1))

print(np.char.replace(str1, "Machine Learning", "ML"))
