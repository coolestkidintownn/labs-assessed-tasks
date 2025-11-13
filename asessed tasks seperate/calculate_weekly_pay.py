def calculate_weekly_pay(hours):
    pay = 0

    if hours > 0:
        if hours <= 35:
            pay = hours * 12
        elif hours > 35:
            pay = 35 * 12
            overtime = hours - 35
            pay = pay + (overtime * 18)
        
        return pay
    
    else:
        print("input must be positive")

print(calculate_weekly_pay(30))
print(calculate_weekly_pay(36))