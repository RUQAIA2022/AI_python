# a == b #equality operator
# a != b #not equal operator
# a > b #greater than operator
# a < b #less than operator
# a >= b #greater than or equal to operator
# a <= b #less than or equal to operator

# if condition is true:
#     execute this block of code

a = 10
b = 10

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")

else:
    print("a is equal to b")


    x = 41

if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("and is also greater than 20")
    else:
        print("but is not greater than 20")

x = 9

if x > 10:
    print("x is greater than 10")

    if x > 20:
        print("and is also greater than 20")
    else:
        print("but is not greater than 20")

else:
    print("x is not greater than 10")  

age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license to drive")

else:
    print("You are too young to drive")    

age = 17
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license to drive")
else:
    print("You are too young to drive")          


if age >= 18 and has_license:
    print("You can drive")    
