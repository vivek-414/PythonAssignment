file_name = input("Enter the file name to read: ")

try:
    with open(file_name, "r") as file:
        contents = file.read()
        print("File contents:")
        print(contents)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
