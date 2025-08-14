list=[True, 23,24,'c',"Sahil",28.34] # Hetero

l=[10,20,30,40,50]
print(l[0])

# last
print(l[-1])

# last not include
print(l[2:5])

# till Last Element
print(l[2:5] == l[2:])

#from 0th to nth-1
print(l[:4])

####### Modify
l[2]=300
print(l)

# Append to last
l.append(60)
print(l)

# At Specific index
l.insert(0,0)
print(l)

# Remove 1st occurrence
l.remove(0)
print(l)

# Remove and Return the last Element
ret=l.pop()
print(ret)

#get index
print(l.index(50))

# Sort
l.sort()
print(l)

############# Slicing
l=[10,20,30,40,50,60,70,80,90]
print(l[0:4])

#Steps 2
print(l[::2])

#Reverse with Steps
print(l[::-1])

############################## Enumerate -> Use for index and Element #######################
l=[10,20,30,40,50,60,70,80,90]
for ind, ele in enumerate(l):
    print(f'index: {ind}, Element: {ele}')


####################### List Comprehension #####################

# Syntax             ->     [item for item in range(xyz)]
# Conditional Syntax ->     [item for item in range(xyz) if condition ]

evenList=[n for n in range(1,11) if n%2==0]
print(evenList)

print("###################################################################################################")

# Student Marks Analyzer

# Step 1: Initial list of student marks
marks = [78, 85, 62, 90, 88]
print("Initial Marks:", marks)

# Step 2: Add a new mark
marks.append(95)
print("After Adding 95:", marks)

# Step 3: Insert a mark at a specific position
marks.insert(2, 70)  # Insert at index 2
print("After Inserting 70 at index 2:", marks)

# Step 4: Remove a specific mark
marks.remove(62)
print("After Removing 62:", marks)

# Step 5: Sort marks in ascending order
marks.sort()
print("Sorted Marks:", marks)

# Step 6: Get top 3 marks (highest)
top_3 = sorted(marks, reverse=True)[:3]
print("Top 3 Marks:", top_3)

# Step 7: Calculate average mark
average = sum(marks) / len(marks)
print("Average Marks:", round(average, 2))

# Step 8: Use list comprehension to find marks > average
above_avg = [m for m in marks if m > average]
print("Marks above average:", above_avg)


# Student Management System using Lists

students = [
    ["Alice", [85, 78, 92]],
    ["Bob", [72, 68, 80]],
    ["Charlie", [90, 88, 95]],
    ["David", [66, 70, 72]],
    ["Eva", [95, 94, 98]]
]

# Function to calculate average marks
def average(marks):
    return round(sum(marks) / len(marks), 2)

# 1️⃣ Display all students with their average
print("\nAll Students with Average Marks:")
for name, marks in students:
    print(f"{name}: {marks} → Avg: {average(marks)}")

# 2️⃣ Add a new student (user input)
name = input("\nEnter new student name: ")
marks = list(map(int, input("Enter 3 marks separated by space: ").split()))
students.append([name, marks])

# 3️⃣ Search for a student
search_name = input("\nEnter name to search: ")
found = False
for student in students:
    if student[0].lower() == search_name.lower():
        print(f"Found {student[0]} → Marks: {student[1]}, Avg: {average(student[1])}")
        found = True
        break
if not found:
    print("Student not found.")

# 4️⃣ Get topper based on average marks
topper = max(students, key=lambda x: average(x[1]))
print(f"\nTopper: {topper[0]} with Avg: {average(topper[1])}")

# 5️⃣ List students scoring above 80 average
above_80 = [name for name, marks in students if average(marks) > 80]
print("Students with Avg > 80:", above_80)

# 6️⃣ Sort by average marks (descending)
students.sort(key=lambda x: average(x[1]), reverse=True)
print("\nSorted by Average Marks:")
for name, marks in students:
    print(f"{name}: Avg {average(marks)}")


