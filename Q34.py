def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            return False
    return True
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")