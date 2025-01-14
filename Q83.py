file_name = "example.txt"
search_string = input("Enter the substring to search: ")

with open(file_name, "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines, start=1):
        if search_string in line:
            print(f"Found in line {i}: {line.strip()}")
