operator = input("""
                enter operator from this list:
                    - "+" for addition
                    - "-" for subtraction
                    - "*" for multiplication
                    - "/" for division (remember to not add 0 or negative numbers as the second number)
                    - "%" for modulus (remember that input will be converted to a whole number)
                    - ">" for greater than comparison
                    - ">=" for greater than or equal to comparison
                    - "<" for less than comparison
                    - "<=" for less than or equal to comparison
                """)

num1 = float(input("enter first number "))
num2 = float(input("enter second number "))

def calculator(num1, num2, operator):
    """
    This function performs basic arithmetic and comparison operations on two numbers.

    Parameters:
    num1 (int or float): The first number.
    num2 (int or float): The second number.
    operator (str): A string representing the operation to perform. The valid operators are:
        - "+" for addition
        - "-" for subtraction
        - "*" for multiplication
        - "/" for division
        - "%" for modulus
        - ">" for greater than comparison
        - ">=" for greater than or equal to comparison
        - "<" for less than comparison
        - "<=" for less than or equal to comparison

    Returns:
    result: The result of the arithmetic operation or comparison. The type of the result depends on the operator:
        - int or float for arithmetic operations
        - bool for comparison operations

    Example Usage:
    --------------
    calculate(4, 5, "*")  # Output: The result is: 20
    calculate(10, 2, "/")  # Output: The result is: 5.0
    calculate(7, 7, ">=")  # Output: The comparison result is: True

    Note:
    -----
    - If division by zero is attempted, the function prints an error message and does not return a result.
    - If an invalid operator is provided, the function prints an error message and does not return a result.
    """
    result = "null"

    if operator == "+":
        result = num1 + num2
        print(f"The result is: {result}")
    elif operator == "-":
        result = num1 - num2
        print("the result is ",result)
    elif operator == "*":
        result = num1 * num2
        print("the result is ",result)
    elif operator == "/":
        if num2 > 0:
            result = num1 / num2
            print("the result is ",result)
        else:
            print("second number must not be 0 or a negative number.")
    elif operator == "%":
        if num2 > 0:
            result = int(num1) % int(num2)
            print("the result is ",result)
        else:
            print("second number must not be 0 or a negative number.")
    elif operator == ">":
        if num1 > num2 == True:
            result = True
        else:
            result = False

        print("the result is ",result)
    elif operator == ">=":
        if num1 >= num2 == True:
            result = True
        else:
            result = False
            
        print("the result is ",result)
    elif operator == "<":
        if num1 < num2 == True:
            result = True
        else:
            result = False
            
        print("the result is ",result)
    elif operator == "<=":
        if num1 <= num2 == True:
            result = True
        else:
            result = False
            
        print("the result is ",result)
    # Function implementation here ...
    else:
        print("Invalid operator.")

    return result

calculator(num1, num2, operator)

## Run the example
# calculator(4, 5, "*")  # Output: The result is: 20
# calculator(10, 2, "/")  # Output: The result is: 5.0
# calculator(7, 7, ">=")  # Output: The comparison result is: True

#loop based code can't use that irritating
""""
        if len(operator) > 1:
            print("enter only one operator")
        else:
            break
    operator_list = ["+","-","*","/","%",">",">=","<","<="]
    loopthing = False
    for i in range(len(operator_list)):
        print(i)
        if operator_list[i] == operator:
            print("nice")
            loopthing = True
            break
    
    if loopthing == True:
        break
    else:
        print("select an operator from the list")
"""