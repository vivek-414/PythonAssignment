numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the number to count: "))
count = 0
for char in numbers:
    if(char==target):
        count+=1
print("Count is ",count)
