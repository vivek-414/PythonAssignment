# 50. LCM
def gcd(a,b):    
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
print(f"The LCM of {a} and {b} is: {lcm(a, b)}")
