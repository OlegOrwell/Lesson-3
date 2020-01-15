
newsum = 0
while True:
    input_list = input("Enter a list numbers or elements separated by space or 'q' to exit the program: ")
    list_1 = input_list.split()
    print("user list is ", list_1)

    sum = 0
    for i in range(0, len(list_1), 1):
        if list_1[i].isdigit() == True:
            sum = sum + int(list_1[i])
        elif list_1[i] == "q":
            newsum = newsum + sum
            print(newsum)
            exit()
        else:
            continue
    newsum = newsum + sum
    print(newsum)

