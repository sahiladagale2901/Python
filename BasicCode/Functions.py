def funtionName():
    # body
    return 0


def evenOdd(num):
    if num % 2 == 0:
        print(f'{num}: Even')
    else:
        print(f'{num}: Odd')


####### Return

def returnSum(a, b):
    return a + b


## Calling function

evenOdd(10)
returnSum(10, 12)


####################### Default Parameters
def great(name):
    print(f'Hello {name.title()}')


great("sahil adagale")


####################### positional

def printNum(*args):
    for i in args:
        print(i, end=' ')


printNum(1, 2, 3, 4, 5, 6, 'Sahil')
print()


######################### Key word arguments

def keyWord(**kwargs):
    for key, val in kwargs.items():
        print(f'{key}: {val}')


keyWord(name="Sahil", age=27)


############################ Both
def both(*args, **kwargs):
    for i in args:
        print(i, end=' ')
    print()
    for key, val in kwargs.items():
        print(f'{key}: {val}')


########################## Temp conversion

def tempConversion(temp, unit):
    if unit == 'C':
        return temp * 9 / 5 + 32
    elif unit == 'F':
        return (temp - 32) * 5 / 9
    else:
        return None


print(tempConversion(25, 'C'))


##################### Calculate total cost of all Items

def costCal(cart):
    totalCost = 0
    for item in cart:
        totalCost += item['price'] * item['quantity']
        print(totalCost)


cart = [
    {'name': 'Apple', 'price': 0.5, 'quantity': 4},
    {'name': 'Banana', 'price': 0.3, 'quantity': 6},
    {'name': 'Orange', 'price': 0.7, 'quantity': 3}
]

costCal(cart)


######################### Palindrome

def palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


print(palindrome("A man a plan a canal Panama"))
