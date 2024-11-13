def find_maximum_difference(a, b):
    # code implementation here...
    
    if (max(a) - min(b)) > (max(b) - min(a)):
        maximum = max(a) - min(b)
    else:
        maximum = max(b) - min(a)
    
    return maximum

print(find_maximum_difference([1,5,600], [100,7,3,602,39]))

