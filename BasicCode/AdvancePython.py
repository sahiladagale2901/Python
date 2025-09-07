### Iterator
from astroid.decorators import yes_if_nothing_inferred

li = [1, 2, 3, 4, 5, 6, 7]
iterator = iter(li)
print(type(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

### Generators -> way to create iterators. Use yield keyword,
#                 produce a series of values lazily, which means they generate
#                 values on the fly and do not store in memory

def sq(n):
    for i in range(3):
        return i**2

print(sq(3)) # its return 1st element only -> 0

def sq(n):
    for i in range(3):
        yield i**2

print(sq(3))

# return the object
for i in sq(3):
    print(i)

print("############## Another way")
a=sq(3)
print(next(a))
print(next(a))

print("############## my_generator way")
def my_generator():
    yield 1
    yield 2
    yield 3

mygen=my_generator()
print(next(mygen)) # or use loop
print(next(mygen))

print("############ Reading line file")
def read_file(filePath):
    with open(filePath,'r') as file:
        for line in file:
            yield line

readLargeFile=read_file("../File/large_file.txt")

for line in readLargeFile:
    print(line.strip())

print("\n############\n######################## Function copy")

def welcome():
    return "Welcome to advance python"
wel=welcome()
print(wel)
del welcome # not able to delete
print(wel)

print("\n############\n######################## Closers")

def main_welcome():
    msg='welcome'
    def sub_welcome_method():
        print(msg)
        print("Welcome to advance python -> sub_welcome_method ")
        # return 0   if return is not present then return None

    return sub_welcome_method()

print(main_welcome())

print("\n############\n######################## Closers -> nested method")

def main_welcome():
    msg='welcome'
    def sub_welcome_method():
        print(msg)
        print("Welcome to advance python -> sub_welcome_method ")
        # return 0   if return is not present then return None

    return sub_welcome_method()

print(main_welcome())

print("\n############\n######################## Decorators")

def main_welcome(func):
    msg='welcome'
    def sub_welcome_method():
        func()
        print("Welcome to advance python -> sub_welcome_method ")
        # return 0   if return is not present then return None

    return sub_welcome_method()

def course_intro():
    print("Advance course")

main_welcome(course_intro)

@main_welcome
def course_intro():
    print("\nAdvance course-> after annotation ")
