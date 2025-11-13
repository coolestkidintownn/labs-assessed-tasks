def calculator(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
        print(f"the result is: {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"the result is: {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"the result is: {result}")
    elif operator == "/":
        if num2 > 0:
            result = num1 / num2
            print(f"the result is: {result}")
        else:
            print("second number cannot be negative or 0") # dividing by zero would cause an error, check happens before calculation is done to avoid this
            result = None
    elif operator == "%":
        if num2 > 0:
            result = int(num1) % int(num2)
            print(f"the result is: {result}")
        else:
            print("second number cannot be negative or 0")
            result = None # had to set a value to result, as i put put return result at the end of the function, and returning a nonexistent variable would return an error
    elif operator == ">":
        if num1 > num2 == True:
            result = True
        else:
            result = False
        print(f"the result is: {result}")
    elif operator == "<":
        if num1 < num2 == True:
            result = True
        else:
            result = False
        print(f"the result is: {result}")
    elif operator == ">=":
        if num1 >= num2 == True:
            result = True
        else:
            result = False
        print(f"the result is: {result}")
    elif operator == "<=":
        if num1 <= num2 == True:
            result = True
        else:
            result = False
        print(f"the result is: {result}")
    else:
        print("invalid operator")
        result = None

    return result

calculator(10, 5, "+")   # 15
calculator(10, 5, "-")   # 5
calculator(10, 5, "*")   # 50
calculator(10, 0, "/")   # "Cannot divide by zero!"
calculator(10, 5, "/")   # 2.0
calculator(10, 5, ">")   # True
calculator(10, 5, "<=")  # False
calculator(10, 5, "$")   # "Invalid operator!"