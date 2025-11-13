def longest_repetition(text):
    count = 0
    longest = ("", 0)
    text = text + " " # this had to be added to account for the longest repetition being at the end

    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count = count + 1
        else:
            count = count + 1
            if count > longest[1]:
                longest = (text[i], count)
            count = 0
    return longest 



print(longest_repetition("ooohellooom"))
print(longest_repetition("aaabbcaaa"))  
print(longest_repetition("bbbbb"))
print(longest_repetition("banana")) 
print(longest_repetition("abc"))

