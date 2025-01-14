import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def calculate_sum(n):
    return sum(range(1, n + 1))

print("Sum:", calculate_sum(1000000))
