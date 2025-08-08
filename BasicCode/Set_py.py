##   SET

# Non Ordered  - No Index
# No Duplicate

s={23,23,23,45,7,898,7}
print(s)

# List to Set
l=[23,23,23,45,7,898,7]
setList=set(l)
print(setList)

# Adding and Removing
s.add(345678)
print(s)
s.remove(345678)
print(s)

# s.remove(358)   throw error bcz element is not present
# so use discard

########## Discard
s.discard(358)   # Remove if the element is present
print(s)

######## pop Method
ele=s.pop()     # Remove the 1st element
print(ele,s)

########### clear
setList.clear()
print(setList)

############### Element present ?
print(7 in s)

############ Union
set1={2,34,45,67,8,5,2}
set2={0,87,5,4,3,2}

setU=set1.union(set2)
print(setU)

############ Intersection
setI = set1.intersection(set2)
print(setI)

############ Intersection and Update
set1.intersection_update(set2)   # update the set1 as well
print(set1)

############ Difference
print(set2.difference(set1)) # Only those elements that are in set2 but not in set1.

############## Sys diff
print(set2.symmetric_difference(set1))  # not in both all unique

############### Subset
set1={1,2,3,5,8,9,0,0}
set2={4,5,1,2,7,3,6}
print(set1.issubset(set2))

################ Super set
print(set1.issuperset(set2))
print(set2.issuperset(set1))
