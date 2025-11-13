def sum_of_evens(min, max):
    total = 0
    if min > 0:
        if max > 0:        
            for i in range(min, (max+1)):
                if i % 2 == 0:
                    total = total + i
        else:
            print("input must be positive")
            
    else:
        print("input must be positive")
   
    return total

print(sum_of_evens(4, 10))
print(sum_of_evens(12, 21))
print(sum_of_evens(-5, 6))