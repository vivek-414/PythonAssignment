import csv

file_name = "example.csv"
with open(file_name, newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(", ".join(row))
