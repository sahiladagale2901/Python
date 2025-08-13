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

