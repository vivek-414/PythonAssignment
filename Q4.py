print("Enter two numbers for operation: ")
n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
print("Enter choice for operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
n=int(input("Enter choice :"))
if(n==1):
    print("Sum is ",(n1+n2))
elif(n==2):
    print("Difference  is ",(n1-n2))
elif(n==3):
    print("product  is ",(n1*n2))
elif(n==4):
    print("Division  is ",(n1/n2))
else:
    print("Invalid")
    

