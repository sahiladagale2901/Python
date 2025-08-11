""" Unordered, key Value
Key should be unique"""

############## declared

d = {}
print(type(d))

d = dict()
print(type(d))

d = {"name": "Sahil",
     "num": 9765001518,
     'adult': True}
print(d)

################### Accessing

print(d['adult'])

print(d.get('age'))   # get method will not raise error if the key is absent

print(d.get('age','Not Available')) # can provide message
print(d.get('num','Not Available'))

#################### Modifying

d['Location']='Katol'  ### Adding the key
d['num']='7498402844'  ### Editing the value

del d['adult']         ### Delete the key
print(d)

print(d.keys())
print(d.values())
print(d.items())

#################### Shallow copy
d1=d.copy()   # agar direct assign kia toh changes dono meh reflect honge

#################### Iterating
for k in d.keys():
   print(k,end=',')

print()
for k in d.values():
   print(k,end=',')
print()

for k,v in d.items():
   print(k,v)
print()

# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Computer Science"
}

# Printing the dictionary
print("Student Details:", student)

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Adding a new key-value pair
student["grade"] = "A"
print("After adding grade:", student)

# Updating a value
student["age"] = 22
print("After updating age:", student)

# Deleting a key-value pair
del student["course"]
print("After deleting course:", student)

# Looping through dictionary
print("\nLooping through dictionary:")
for key, value in student.items():
    print(f"{key} : {value}")




