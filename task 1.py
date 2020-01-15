def func(arg1, arg2):
    return arg1 / arg2

try:
    arg1 = int(input("Enter first number "))
    arg2 = int(input("Enter second number "))
    print(func(arg1, arg2))

except ZeroDivisionError:
    print("Division by zero error!")