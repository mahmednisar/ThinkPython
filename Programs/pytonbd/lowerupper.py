string = input("Give me a phrase:")
string_up = 0
string_lo = 0
for i in string:
    if i.isupper():
        string_up += 1
    if i.islower():
        string_lo += 1
print("The number of uppercase letters in your phrase is:", string_up)
print("The number of lowercase letters in your phrase is:", string_lo)



        
