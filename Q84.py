file_name = "example.txt"
line_to_append = input("Enter a line to append to the file: ")

with open(file_name, "a") as file:
    file.write(line_to_append + "\n")

print(f"Line appended to {file_name}.")
