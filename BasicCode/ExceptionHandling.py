# try
# ..............
# except:
# ................
#
#

######################### Multiple Except block #######################
try:
    a = 10 / 0
except ZeroDivisionError as ex:
    print(ex)
except Exception as ex:  ## Base class
    print(ex)

########################### Base Class Use ##############################
try:
    a = 10 / 2
    a = b
except ZeroDivisionError as ex:
    print(ex)
except Exception as ex:  ## Base class
    print(ex)

############################## Valur Error #############################
try:
    a = int('abc')
except ValueError as ex:
    print(ex)

############################### Else block #############################
try:
    a = 10 / 2
except ZeroDivisionError as ex:
    print(ex)

# if the except block is not executed then else will
else:
    print(f"result is {a}")

############################### Finally Block ###########################
try:
    a = 10 / 5
except ZeroDivisionError as ex:
    print(ex)

# if the except block is not executed then else will
else:
    print(f"else block -> result is {a}")

# Its always executed no matter what
finally:
    print("finally block always executed no matter what")
