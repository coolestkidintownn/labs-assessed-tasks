def maximum_gap(list1, list2):
    diff1 = max(list1) - min(list2)
    diff2 = max(list2) - min(list1)

    if diff1 > diff2:
        return diff1
    else:
        return diff2
    
print(maximum_gap([1,5 ,600], [100 ,7, 3 , 29, 39])) 
print(maximum_gap([1,5 ,600], [100 ,7, 3 , 602, 39]))