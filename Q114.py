# List comprehension
list_comp = [x * x for x in range(1, 10001)]
print("List Comprehension Done")

# Generator expression
gen_expr = (x * x for x in range(1, 10001))
print("Generator Expression Created")

# Iterate through the generator (no memory overhead)
for _ in range(10):  # Display first 10 squares
    print(next(gen_expr), end=" ")
