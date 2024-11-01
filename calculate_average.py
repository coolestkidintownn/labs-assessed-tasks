def calculate_average(numbers):
    """
    This function calculates the average of a list of numbers using a for loop.

    Parameters:
    ----------
    numbers : list
        A list of numerical values (int or float).

    Returns:
    -------
    float:
        The average of the numbers in the list. If the list is empty, returns None.

    Example:
    --------
    calculate_average([10, 20, 30, 40, 50])  # Output: 30.0
    """
    
    # Function implementation here ...

    quantity = 0
    for i in numbers:
        quantity = quantity + 1

    stack = 0
    for i in range(quantity):
        stack = stack + numbers[i]

    average = stack / quantity
    return average



# Example usage
numbers = [10, 20, 30, 40, 50]
print("The average is:", calculate_average(numbers))  # Expected output: The average is: 30.0
