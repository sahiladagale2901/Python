import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

### Element wise add
print("Addition: ", arr1 + arr2)

### Element wise Sub
print("Substraction: ", arr1 - arr2)

### Element wise Mul
print("Multiplication: ", arr1 * arr2)

### Element wise Div
print("Division: ", (arr2 // arr1))

#################### Universal Function

arr = np.array([1, 2, 3, 4, 5])
print("Square root: ", np.sqrt(arr))
print("Exponential:", np.exp(arr))
print("Sine:", np.sin(arr))
print("Natural log:", np.log(arr))

#################### Slicing and Indexing
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [11, 22, 33, 44, 55]])

print("1st of 1st ele: ", arr[0][0])
print("3rd of 2nd ele: ", arr[2][1])
print("2nd row: ", arr[1:2])
print("2nd and 3rd row:\n ", arr[1:3])
print("or:\n ", arr[1:])

#################### Modify Elements
arr[1][4] = 10
print(arr)

#################### Logical Operation
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("data>5 -> gives boolean:\n ", data > 5)
print("data[data>5]-> gives data:\n ", data[data > 5])
print("data[(data > 5) & (data <= 9)]-> gives:\n ", data[(data > 5) & (data <= 9)])
