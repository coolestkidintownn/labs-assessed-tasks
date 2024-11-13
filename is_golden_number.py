def is_golden_number(n):
    # function implementation ...

    if n < 1000:
        for a in range(1, n):
            b = n - a  
            if b > 0:
                if (a * b) % 1000 == 0:
                    return True
            
        return False
    else:
        print("number is too large")

print(is_golden_number(61))

