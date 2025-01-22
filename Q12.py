
str = str(input("Enter a string: "))
rev=str[::-1]
if (str==rev):  #string slicing
    print("Palindrome")
else:
    print("Not Palindrome")