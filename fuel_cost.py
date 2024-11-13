def fuel_cost(distance_miles):
    # Constants
    # MPG = 50  # Miles per gallon
    # LITERS_PER_GALLON = 4.5
    # PRICE_PER_LITER = 1.49  # Price in pounds per liter
    # continue function implementation here...

    total_cost = ((distance_miles / 50) * 4.5) * 1.49

    return total_cost

print(fuel_cost(50))

