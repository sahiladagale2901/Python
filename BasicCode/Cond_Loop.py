age =30

if age >= 18:
    print('Adult')
elif age<18:
    print('Teen')
else:
    print('invalid input')

# Logical

sub1=80
sub2=60

if sub1>60 and sub2>60:
        print('Garde 1')
elif sub1>50 and sub2>50:
    print('grade 2')
else:
    print('fail')


######################## leap Year ####################################

# yr=int(input('Enter and Year: '))
yr=2000

if ((yr%4 == 0 and yr%100 != 0) or yr%400==0):
    print('Leap Yr')
else:
    print('Not a leap yr')

###########################  LOOP #####################################

########### While :
i = 1
while(i<=5):
    print(i,end=' ')
    i+=1
print()

################# For :
for i in range(6):
    print(i,end=' ')
print()

for i in range(10,1,-1):
    print(i,end=' ')
print()

s='Sahil'
for char in s:
    print(char,end=' ')
print()

for char in range(len(s)-1,-1,-1):
    print(s[char],end=' ')
print()

########################### Factorial ########################
fact=1
for i in range(1,6):
    fact=fact*i

print(f"Factorial of 5 is {fact}")

########### ############# Sum Of 1st N Natural Num ###################

sum=0; nth=10
n=nth
while n>0:
    sum=sum+n
    n-=1
print(f"Sum of 1st {nth}th Num is: {sum}")

########################## Prime Num ##############################3
for num in range(1,101):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,end=' ')

print()






