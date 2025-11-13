def sum_of_digits(num):
    total = 0
    num = str(num)

    for i in num:
        i = int(i)
        total = total + i

    return total

print(sum_of_digits(445))

        