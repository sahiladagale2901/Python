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
    for j in range(i,len(lt) - 1):

        if lt[i] > lt[j]:
            temp=lt[j]
            lt[j]=lt[i]
            lt[i]=temp

print(lt)
print(f"Largest of the above list is : {lt[len(lt)-1]}")
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

li=[0,1,1,0,0,0,1,1,1,0,1,0,1,0]

li_1=[]
li_0=[]

for i in li:
    if li[i]==0:
        li_0.append(li[i])
    else:
        li_1.append(li[i])

print(li_0+li_1)
print(li_1)


###############

# String Program in Python

# Input from user
text = input("Enter a string: ")

# 1. Length of string
print("\nLength of string:", len(text))

# 2. Convert to uppercase and lowercase
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# 3. Reverse the string
print("Reversed string:", text[::-1])

# 4. Count vowels in the string
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)

# 5. Check if string is palindrome
if text == text[::-1]:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")

# 6. Replace spaces with hyphens
print("With hyphens:", text.replace(" ", "-"))

