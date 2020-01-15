def int_func(list_1):

    word = list(list_1)
    first_letter = word[0].upper()
    word[0] = first_letter
    slovo = " "
    for i in range(0, len(word), 1):
        slovo = slovo + word[i]
    return slovo


text = input("Enter any group of words starting with lower case ")
List = text.split()
logo = ""
for t in range(0, len(List), 1):
    list_1 = List[t]
    int_func(list_1)
    logo = logo + int_func(list_1)

print(logo)

