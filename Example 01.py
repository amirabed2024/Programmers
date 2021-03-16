def CharChange(str):
    NewString = ""
    for i in range(0, len(str)):
        if str[i].islower()==True:
            NewString += str[i].upper()
        else:
            NewString += str[i].lower()
    return NewString
str = input("Enter:")
str = CharChange(str)
print("Output is:",str)