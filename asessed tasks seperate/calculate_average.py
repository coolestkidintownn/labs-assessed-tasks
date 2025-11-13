def calculate_average(list):
    total = 0
    count = 0

    for i in list:
        count = count + 1
        total = total + i

    average = total / count
    return average


    
print(calculate_average([1, 4, 5, 6]))
print(calculate_average([1, 8, 9]))