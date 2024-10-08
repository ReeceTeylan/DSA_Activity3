def square_of_odds():
    int_list = list(range(1, 21))
# List comprehension, Only include squares of odd numbers
    return [x ** 2 for x in int_list if x % 2 != 0]

# Print the result
print("Square of odd numbers from 1 to 20:", square_of_odds())






