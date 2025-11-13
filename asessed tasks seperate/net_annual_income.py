def net_annual_income(gross_salary):
    taxable_income = gross_salary - 12570
    basic_total = 50270 - 12571
    higher_total = 125140 - 50271
    
    if gross_salary <= 50270:
        tax = taxable_income * 0.2
        final_income = gross_salary - tax

    if 50270 < gross_salary <= 125140:
        taxable_income = taxable_income - basic_total
        tax = taxable_income * 0.4
        final_income = gross_salary - tax - (basic_total * 0.2)
    
    if gross_salary > 125140:
        taxable_income = taxable_income - 125140
        tax = taxable_income * 0.45
        final_income = gross_salary - tax - (basic_total * 0.2) - (higher_total * 0.4)


    return str(final_income)[:len(str(gross_salary))+3]

print(net_annual_income(60000))
print(net_annual_income(32456))
print(net_annual_income(235926))