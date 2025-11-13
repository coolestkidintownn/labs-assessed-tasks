def winning_numbers(winning_list, guessed_list):
    total = 0

    if guessed_list[0] == winning_list[0]: # these sections check each element of the guessed list to each element of the winning list, and adds points to a total accordingly
        total = total + 1
    elif guessed_list[0] == winning_list[1]:
        total = total + 1
    elif guessed_list[0] == winning_list[2]:
        total = total + 1

    if guessed_list[1] == winning_list[0]:
        total = total + 1
    elif guessed_list[1] == winning_list[1]:
        total = total + 1
    elif guessed_list[1] == winning_list[2]:
        total = total + 1

    if guessed_list[2] == winning_list[0]:
        total = total + 1
    elif guessed_list[2] == winning_list[1]:
        total = total + 1
    elif guessed_list[2] == winning_list[2]:
        total = total + 1

    if total == 0: # uses the total to assign the correct result to the prize variable, then returns the prize variable
        prize = "No"
    if total == 1:
        prize = "Third"
    if total == 2:
        prize = "Second"
    if total == 3:
        prize = "First"
    
    return prize


# Test cases
print(winning_numbers([5, 14, 17], [5, 14, 6])) # Expected: "Second"
print(winning_numbers([1, 2, 3], [1, 2, 3])) # Expected: "First"
print(winning_numbers([4, 7, 9], [0, 7, 2])) # Expected: "Third"
print(winning_numbers([10, 20, 30], [0, 0, 0])) # Expected: "No"