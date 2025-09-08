import numpy as np

arr1=np.array([1,2,3,4,5,6])
print(arr1)
print(type(arr1))
print(arr1.shape)

arr2=arr1.reshape(2,3) # 2 rows, 3 column
print(arr2)

arr2=np.array([[1,2,3,4,5,6],[0,9,8,7,6,5]])
print(arr2.shape)

print(np.ones((2,2),int))
print(np.zeros((2,2)))
