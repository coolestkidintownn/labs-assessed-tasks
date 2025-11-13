def are_anagrams(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    length1 = 0
    length2 = 0
    for i in word1:
        length1 = length1 + 1
    for i in word2:
        length2 = length2 + 1

    count = 0
    if length1 == length2:
        for i in word1:
            for j in word2:
                if i == j:
                    count = count + 1
    else: 
        return False
      
    if count == length1: # i don't think an identical word is an anagram, if it is then this should be
        return True      # if count => length1 however i left it as ==
    else:
        return False
    

print(are_anagrams("heart", "Earth"))
print(are_anagrams("help", "self"))
print(are_anagrams("little", "litle"))
print(are_anagrams("bIllY", "BILLY"))
print(are_anagrams("bob", "bob"))
