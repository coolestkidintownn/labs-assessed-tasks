def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams of each other.

    Parameters:
    ----------
    str1 : str
        The first string to be compared.
    str2 : str
        The second string to be compared.

    Returns:
    -------
    bool:
        Returns True if the two strings are anagrams, otherwise False.

    Example:
    --------
    are_anagrams("listen", "silent")  # Output: True
    are_anagrams("hello", "world")    # Output: False
    """

    # Function implementation here ...

    length = 0
    for i in str1:
        length = length + 1      # function to find length of the string
    

    # list_thing1 = [0] * length
    # for i in range(length):
    #     list_thing1[i] = str1[i]         # creates list of length of the string and puts each character in it, didn't need it in the end

    # list_thing2 = [0] * length
    # for i in range(length):
    #     list_thing2[i] = str2[i]

    count = 0
    for j in range(length):
        for i in range(length):
            if str1[j] == str2[i]:
                count = count + 1       # goes through every element of both strings and checks if they are the same, and then creates a total
                break
    
    if count == length:      # checks if total count is the same as length meaning it is a perfect anagram
        return True
    else:
        return False

            


    print(str1)
    print(str2)
    


print(are_anagrams("hello", "olleh"))

## Example 
# print(are_anagrams("listen", "silent"))  # Expected output: True
# print(are_anagrams("hello", "world"))    # Expected output: False

