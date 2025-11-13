def password_strength(password):
    length = 0
    specialCharacters = ["@", "$", "£"]
    specialCheck = False
    upperCheck = False

    for i in password:
        length = length + 1
        for j in specialCharacters:
            if specialCheck == False:
                if i == j:
                    specialCheck = True
        if i.isupper() == True:
            upperCheck = True

    if length < 6 or specialCheck == False or upperCheck == False:
        return "Weak"
    elif length <= 10 and specialCheck == True and upperCheck == True:
        return "Medium"
    else:
        return "Strong"
    
print(password_strength("abc"))
print(password_strength("Abc@12"))
print(password_strength("MyPass$2025"))