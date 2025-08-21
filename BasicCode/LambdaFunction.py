# lambda variable:Expresion

def add(a, b):
    return a + b


addition = lambda a, b: a + b

print(addition(12, 12))
print(type(addition))

even = lambda num: num % 2 == 0

print(even(4))


##################################################################################
########## MAP
def sq(n):
    return n * n


num = [1, 2, 3, 4, 5, 6]
print(list(map(sq, num)))

# with Lambda

print(list(map(lambda x: x * x, num)))

num1 = [1, 2, 3]
num2 = [4, 5, 6]

addedList = list(map(lambda x, y: x + y, num1, num2))

print(addedList)

###############################################################################

# Filter Function
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
even_list = list(filter(lambda x: x % 2 == 0, li))

print(even_list)

even_greater5list = list(filter(lambda x: x % 2 == 0 and x > 5, li))
print(even_greater5list)

# age is greater than 25 in dICT

people = [
    {"name": "Rahul", "age": 21},
    {"name": "sai", "age": 27},
    {"name": "Sub", "age": 30}
]

fil=filter 
