def my_func(arg1, arg2, arg3):
    a = min(arg1, arg2, arg3)
    return arg1 + arg2 + arg3 - a

arg1 = int(input("Enter first number "))
arg2 = int(input("Enter second number "))
arg3 = int(input("Enter third number "))

print(my_func(arg1, arg2, arg3))