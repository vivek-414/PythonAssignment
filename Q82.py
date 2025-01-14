file_name = "example.txt"
with open(file_name, "r") as file:
    words = file.read().split()
    longest_word = max(words, key=len)
    print(f"The longest word in {file_name} is: {longest_word}")
