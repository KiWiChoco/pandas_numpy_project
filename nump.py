import numpy as np

list = [0]*10
a = np.array(list)
print(a)

a[4] = 1
print(a)

list1 = range(10,50,1)
b= np.array(list1)
print(b)

list2 = range(0,25,1)
c= np.array(list2).reshape((5,5))
print(c)

d = np.eye(5)
print(d)

