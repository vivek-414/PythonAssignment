import json

data = {
    "name": "Atharv",
    "age": 25,
    "city": "Delhi"
}

# Write JSON to a file
with open("data.json", "w") as file:
    json.dump(data, file)

# Read JSON from the file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

# Modify a value
loaded_data["city"] = "Mumbai"

# Write the updated data back to the file
with open("data.json", "w") as file:
    json.dump(loaded_data, file)

print("Updated JSON:", loaded_data)
