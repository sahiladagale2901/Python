t=(True,23,1233.3,'Sahil')

print(t[0])
print(t[:4])

# Operation

t=(True,23,1233.3,'Sahil',23)
t1=(True,23,1233.3)

print(t+t1)

########### Immutable
# t[0]=0    #TypeError: 'tuple' object does not support item assignment
# print(t)

print(t.count(23))  # two times
print(t.index(23))  # index of 1st occurrence

############## Packing and Unpacking

####### Packing
packed_tuple=1,"Hello",3.14
print(packed_tuple)

####### Unpacking
a,b,c=packed_tuple
print(a,b,c)

####### Unpacking with *
num=(9,8,7,6,5,4,3,2,1)
*first,mid,last=num
print(first,mid,last)

first,*mid,last=num
print(first,mid,last)

first,mid,*last=num
print(first,mid,last)

# Same for list as well
# num=[9,8,7,6,5,4,3,2,1]
# *first,mid,last=num
# print(first,mid,last)

########### Nested Tuple

nt=((12,123,123,45),('dfg','df'))
print(nt[1][0])