def closest_pair_under_budget(prices, budget):
    budget_dict = {}
    sort = []

    for i in range(len(prices)):
        for j in range (len(prices)):
            if prices[i] != prices [j]:
                comparitor = (prices[i][1] + prices[j][1]) 
                if comparitor <= budget: 
                    budget_dict[(prices[i][0], prices[j][0])] = comparitor # create dict of all combinations of the item things, using only values that are less than oq eqaual to budget

    for i in budget_dict.values():
        sort.append(i)


    sorted = False
    sortedCheck = 0 
    while sorted == False:
        for i in range(len(sort)):
            if sort[i-1] > sort[i]:
                sort.append(sort[i-1])
                sort.pop(i-1)
            else:
                sortedCheck = sortedCheck + 1 # sort list algorithm from a prior task
        if sortedCheck > len(sort)+1:
            sorted = True
            print(sort)


    for i in budget_dict.items(): # iterates through dict to find the first instance of the highest price on sorted list
        if i[1] == sort[-1]:
            return i[:1] 
            break


    





items = [("tv", 300), ("mobile phone", 800), ("laptop", 600), ("headphones", 200)]
budget1 = 1000
print(closest_pair_under_budget(items, budget1))