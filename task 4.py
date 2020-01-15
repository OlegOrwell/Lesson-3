def my_func(arg1, arg2):
    return arg1**arg2
def my_func2(arg1, arg3):
    result = 1
    for i in range(0, arg3, 1):
        result = result * 1/(arg1)
    return result


x = int(input("Enter first number "))
y = int(input("Enter second number "))

arg1 = abs(x)
arg2 = 0 - abs(y)
arg3=abs(y)
print(arg1)
print(arg2)
print(my_func(arg1, arg2))
print(my_func2(arg1, arg3))

