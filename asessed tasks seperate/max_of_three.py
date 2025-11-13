def max_of_three(num1, num2, num3):
    maximum = None

    if num1 > num2:
        if num1 > num3:
            maximum = num1
    elif num2 > num3:
        maximum = num2
    else:
        maximum = num3 # can just use else here without any comparison because it is already established at this point that it must be greater than num1 and 2 if this is executed

    return maximum

print(max_of_three(10, 20, 30))# Output: 30
print(max_of_three(5, 12, 8)) # Output: 12
print(max_of_three(40.1, -5, 10)) # Output: 40.1