##################### Count vowels in a string #########################

str1 = "education"
smallVowels = ['a', 'e', 'i', 'o', 'u']
capsVowels = ['A', 'E', 'I', 'O', 'U']
count = 0
for char in str1:
    if (char in smallVowels) or (char in capsVowels):
        count += 1
print(count)
########################################################################################################################

############### Alternate:

vowels = 'aeiouAEIOU'
count = 0
for char in str1:
    if char in vowels:
        count += 1
print(count)
########################################################################################################################

############### Comprehension:

count1 = tuple(char for char in str1 if char in vowels)  ########### Tuple -> Explicit
print(len(count1))

count1 = ([char for char in str1 if char in vowels])
print(len(count1))
########################################################################################################################

###############  With Sum Method

count2 = sum(1 for char in str1 if char in vowels)
print(count2)

# --------------------------------------------------------------------------------------------------------------------------------------------------
# ==================================================================================================================================================
# --------------------------------------------------------------------------------------------------------------------------------------------------

####################################### Find duplicate elements in a list ##############################################

# l = [22, 2345, 56, 65, 56, 6587, 3, 2, 11, 11, 44]
# count = 1
# for i in range(len(l) - 1):
#     for j in range(i+1, len(l) - 1):
#         if l[i] == l[j]:
#             count += 1
#         break
#
#     print(f"{l[i]} occur {count} times")

l = [22, 2345, 56, 65, 56, 6587, 3, 2, 11, 11, 44]
d = {}
count = 1
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

# --------------------------------------------------------------------------------------------------------------------------------------------------
# ==================================================================================================================================================
# --------------------------------------------------------------------------------------------------------------------------------------------------

################################################### Find the largest numbers from the list #################################################
lt = [2, 34, 2, 456, 32467, 256, 9098]
lt.sort(reverse=True)
print(f"largest number from the list is: {lt[0]}")
print(f"smallest number from the list is: {lt[len(lt) - 1]}")  # or print(f"smallest number from the list is: {lt[-1]}")

############# Without Sort method

lt = [2, 34, 2, 456, 32467, 256, 9098]

for i in range(len(lt) - 1):
    for j in range(i, len(lt) - 1):

        if lt[i] > lt[j]:
            temp = lt[j]
            lt[j] = lt[i]
            lt[i] = temp

print(lt)
print(f"Largest of the above list is : {lt[len(lt) - 1]}")
print(f"Smallest of the above list is : {lt[0]}")

# --------------------------------------------------------------------------------------------------------------------------------------------------
# ==================================================================================================================================================
# --------------------------------------------------------------------------------------------------------------------------------------------------

############################################# Dict List and Set ######################################

# -------------------------------
# Example: Students & Subjects
# -------------------------------

# List of student names
students = ["Amit", "Priya", "Rohit", "Amit", "Neha", "Priya"]

# Remove duplicates using a set
unique_students = set(students)
print("Unique Students:", unique_students)

# Dictionary to store student -> subjects mapping
student_subjects = {
    "Amit": ["Math", "Physics"],
    "Priya": ["Biology", "Chemistry"],
    "Rohit": ["History", "Geography"],
    "Neha": ["Computer", "Math"]
}

# Add a new student from the set to dict (if not present)
for student in unique_students:
    if student not in student_subjects:
        student_subjects[student] = []

# Print dictionary
print("\nStudent Subjects:")
for name, subjects in student_subjects.items():
    print(f"{name}: {subjects}")

# Find all unique subjects across all students (set + list comprehension)
all_subjects = {subj for subs in student_subjects.values() for subj in subs}
print("\nAll Unique Subjects:", all_subjects)

# Convert the set of subjects to a sorted list
sorted_subjects = sorted(list(all_subjects))
print("Sorted Subjects List:", sorted_subjects)

# --------------------------------------------------------------------------------------------------------------------------------------------------
# ==================================================================================================================================================
# --------------------------------------------------------------------------------------------------------------------------------------------------

########################################## separate 1 and 0 #################################

li = [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0]

li_1 = []
li_0 = []

for i in li:
    if li[i] == 0:
        li_0.append(li[i])
    else:
        li_1.append(li[i])

print(li_0 + li_1)
print(li_1)

###############

# String Program in Python

# Input from user
# text = input("Enter a string: ")
#
# # 1. Length of string
# print("\nLength of string:", len(text))
#
# # 2. Convert to uppercase and lowercase
# print("Uppercase:", text.upper())
# print("Lowercase:", text.lower())
#
# # 3. Reverse the string
# print("Reversed string:", text[::-1])
#
# # 4. Count vowels in the string
# vowels = "aeiouAEIOU"
# count = sum(1 for char in text if char in vowels)
# print("Number of vowels:", count)
#
# # 5. Check if string is palindrome
# if text == text[::-1]:
#     print("Palindrome: Yes")
# else:
#     print("Palindrome: No")
#
# # 6. Replace spaces with hyphens
# print("With hyphens:", text.replace(" ", "-"))


######################################################### Sum of the Digit ###########################

intNum = 123123
sum = 0
for i in str(intNum):
    sum += int(i)

print(sum)


#####################################################################################################
def calculate_y(slope, intercept, x):
    """
    Function to calculate the value of y using the slope-intercept form of a line.

    Parameters:
    slope (float): The slope of the line.
    intercept (float): The y-intercept of the line.
    x (float): The value of x for which y needs to be calculated.

    Returns:
    float: The calculated value of y.
    """
    # Your code here

    return slope * x + intercept


######################################################################################################

def sum_list(numbers):
    total = 0

    for i in numbers:
        total += i

    return total


######################################################################################################
def find_largest(numbers):
    sorted_numbers = sorted(numbers, reverse=True)

    return sorted_numbers[0]


######################################################################################################
def remove_duplicates(lst):
    s = list(set(lst))
    return s


######################################################################################################

# Check if all elements in a List are Unique

def check_unique(lst):
    lst = sorted(lst, reverse=False)

    set_list = list(set(lst))

    if set_list == lst:
        return True
    else:
        return False


######################################################################################################
def reverse_list(lst):
    return lst[::-1]


######################################################################################################
def count_even_odd(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd
#####################################################################################################
def is_subset(lst1, lst2):
    set1=set(lst1)
    set2=set(lst2)
    return set1.issubset(set2)

#####################################################################################################
# Student Marks Management System

def add_student(students, name, marks):
    """Add a student and their marks."""
    if name in students:
        print(f"⚠️ {name} already exists. Updating marks...")
    students[name] = marks


def display_students(students):
    """Display all students with marks."""
    if not students:
        print("📂 No student records found.")
        return
    print("\n--- Student Records ---")
    for name, marks in students.items():
        print(f"{name}: {marks}")


def topper(students):
    """Find and display the student with the highest marks."""
    if not students:
        print("❌ No data available to find topper.")
        return
    top = max(students, key=students.get)
    print(f"\n🏆 Topper: {top} ({students[top]} marks)")


def sort_students(students):
    """Sort students by marks in descending order."""
    sorted_students = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))
    print("\n📊 Students sorted by marks:")
    for name, marks in sorted_students.items():
        print(f"{name}: {marks}")


# Main program
students = {}

while True:
    print("\nMenu:")
    print("1. Add/Update Student")
    print("2. Display Students")
    print("3. Find Topper")
    print("4. Sort by Marks")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    if choice == 1:
        name = input("Enter student name: ").strip()
        try:
            marks = int(input(f"Enter marks for {name}: "))
        except ValueError:
            print("❌ Marks must be an integer.")
            continue
        add_student(students, name, marks)

    elif choice == 2:
        display_students(students)

    elif choice == 3:
        topper(students)

    elif choice == 4:
        sort_students(students)

    elif choice == 5:
        print("✅ Exiting program. Goodbye!")
        break

    else:
        print("❌ Invalid choice, try again.")


    ###############################################################################################

    # Python Program on Functions

    # 1. Function without parameters
    def greet():
        print("Hello! Welcome to Python functions.")


    # 2. Function with parameters
    def add_numbers(a, b):
        return a + b


    # 3. Function with default parameter
    def power(base, exponent=2):
        return base ** exponent


    # 4. Function with multiple returns
    def min_max(numbers):
        return min(numbers), max(numbers)


    # -----------------------
    # Calling the functions
    # -----------------------

    # 1. No parameters
    greet()

    # 2. With parameters
    result = add_numbers(5, 7)
    print("Sum of 5 and 7 is:", result)

    # 3. Default parameter
    print("5 squared is:", power(5))
    print("5 to the power of 3 is:", power(5, 3))

    # 4. Multiple return values
    numbers = [4, 8, 1, 9, 2]
    minimum, maximum = min_max(numbers)
    print("Minimum number is:", minimum)
    print("Maximum number is:", maximum)

###############################################################################################
# Example of Method Overloading using default arguments
class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

# Testing
calc = Calculator()
print("Sum of two numbers:", calc.add(10, 20))        # 30
print("Sum of three numbers:", calc.add(10, 20, 30)) # 60
print("Sum with one number:", calc.add(10))          # 10

###############################################################################################

# Example of Method Overriding
class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def sound(self):  # overriding parent method
        print("Dog barks")

class Cat(Animal):
    def sound(self):  # overriding parent method
        print("Cat meows")

# Testing
a = Animal()
a.sound()   # Animals make sounds

d = Dog()
d.sound()   # Dog barks

c = Cat()
c.sound()   # Cat meows


#######################################################################################################
from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass   # abstract method, no body

    @abstractmethod
    def perimeter(self):
        pass

# Concrete Class
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Testing
rect = Rectangle(10, 5)
print("Rectangle Area:", rect.area())         # 50
print("Rectangle Perimeter:", rect.perimeter()) # 30

circle = Circle(7)
print("Circle Area:", circle.area())          # 153.86
print("Circle Perimeter:", circle.perimeter()) # 43.96

##############################################################################################################

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private variable
        self.__balance = balance                # private variable

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Setter for balance (with condition)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Invalid withdraw amount or Insufficient balance")

# Testing
acc = BankAccount("12345", 1000)

# Access through methods (good ✅)
print("Balance:", acc.get_balance())  # 1000
acc.deposit(500)                      # Deposited: 500
acc.withdraw(300)                     # Withdrew: 300
print("Balance:", acc.get_balance())  # 1200
##################################################################################################

# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Derived class (single inheritance)
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
        self.course = course

    def display_info(self):  # Overriding parent method
        super().display_info()
        print(f"Student ID: {self.student_id}, Course: {self.course}")


# Another derived class (multilevel inheritance)
class GraduateStudent(Student):
    def __init__(self, name, age, student_id, course, thesis_topic):
        super().__init__(name, age, student_id, course)
        self.thesis_topic = thesis_topic

    def display_info(self):  # Overriding again
        super().display_info()
        print(f"Thesis Topic: {self.thesis_topic}")


# Derived class with its own method
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")


# Testing the classes
print("---- Person ----")
p1 = Person("Alice", 40)
p1.display_info()

print("\n---- Student ----")
s1 = Student("Bob", 20, "ST101", "Computer Science")
s1.display_info()

print("\n---- Graduate Student ----")
g1 = GraduateStudent("Charlie", 24, "GS202", "AI", "Deep Learning in Healthcare")
g1.display_info()

print("\n---- Teacher ----")
t1 = Teacher("Dr. Smith", 45, "Mathematics")
t1.display_info()

########################################################################################

# File: file_example.py

# 1. Writing to a text file (creates if not exists)
with open("..\File\example.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("Python makes file handling easy!\n")

print("✅ Data written to example.txt")

# 2. Reading from the file
with open("..\File\example.txt", "r") as file:
    content = file.read()
    print("\n📖 File Content:\n")
    print(content)

# 3. Appending new data
with open("..\File\example.txt", "a") as file:
    file.write("This line was appended later.\n")

print("\n✅ Data appended to example.txt")

# 4. Reading line by line
with open("..\File\example.txt", "r") as file:
    print("\n📌 Reading line by line:")
    for line in file:
        print(line.strip())

#########################################################################
# Simple Calculator in Python

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", add(num1, num2))
elif choice == 2:
    print("Result:", subtract(num1, num2))
elif choice == 3:
    print("Result:", multiply(num1, num2))
elif choice == 4:
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice")

###############################################################################
def is_leap_year(year):
    # Leap year rules:
    # 1. Divisible by 4 → leap year
    # 2. Divisible by 100 → not a leap year
    # 3. Divisible by 400 → leap year
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    return False

# Example usage
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a Leap Year ✅")
else:
    print(f"{year} is NOT a Leap Year ❌")





