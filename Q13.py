
input_string = input("Enter a string: ")


reversed_string = input_string[4::-1]  # Reverse the string
skipped_string = input_string[0:6:2]     # Skip every second letter


print(f"Original string: {input_string}")
print(f"Reversed string: {reversed_string}")
print(f"Skipped letters: {skipped_string}")
