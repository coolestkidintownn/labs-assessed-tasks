def sort_list(theList):
    sortedCheck = 0
    sorted = False
    
    length = 0
    for i in theList:
        length = length + 1

    while sorted == False:
        for i in range(length):
            if theList[i-1] > theList[i]:
                theList.append(theList[i-1])
                theList.pop(i-1)
            else:
                sortedCheck = sortedCheck + 1
        if sortedCheck > length+1: # I did length+1 here because i noticed that if i just did length it stopped short one of sorting it
            sorted = True
            return theList
        
print(sort_list([5, 6, 9, 0]))
print(sort_list([1, 2, 1]))
print(sort_list([-10, -1, 9]))
