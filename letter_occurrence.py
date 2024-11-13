def letter_occurrence(input_string):
    # complete function implementation...

    count = 0
    length = 0

    for i in input_string:
        length = length + 1

    for i in range(length):
        if input_string[i] == "a":
            count = count + 1
        elif input_string[i] == "A":
            count = count + 1

    return count

print(letter_occurrence("Amazing apple Actors!"))