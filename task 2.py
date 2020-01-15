def info(**kwargs):
    for a, b in kwargs.items():
        print(a, b)
    print(kwargs.values())

Name = input("Enter man's name ")
Surename = input("Enter man's surename ")
DateOfBirth = input("Enter man's date of birth ")
City = input("Enter city of living ")
Email = input("Enter man's e-mail ")
Phone = input("Enter phone number ")

info(name = Name, surename = Surename, dateofbirth = DateOfBirth, city = City, email = Email, phone = Phone)

