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


#leap Year

# yr=int(input('Enter and Year: '))
yr=2000

if ((yr%4 == 0 and yr%100 != 0) or yr%400==0):
    print('Leap Yr')
else:
    print('Not a leap yr')

#Loop

i = 1
while(i<=5):
    print(i)
    i+=1

for i in range(6):
    print(i,end=' ')

