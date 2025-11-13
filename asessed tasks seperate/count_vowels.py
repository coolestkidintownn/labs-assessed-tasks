def count_vowels(word):
    word = word.lower()
    vowelList = ["a", "e", "i", "o", "u"]
    numVowels = 0

    length = 0
    for i in word:
        length = length + 1
    
    for i in vowelList:
        for j in range(length):
            if word[j] == i:
                numVowels = numVowels + 1
            
    return numVowels



print(count_vowels("Hello World"))
print(count_vowels("Programming is interesting"))
print(count_vowels("Are you okay?"))