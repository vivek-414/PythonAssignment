from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# Reduce to sum even numbers
sum_even = reduce(lambda x, y: x + y, even_numbers)
print("Sum of Even Numbers:", sum_even)
