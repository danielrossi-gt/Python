import csv

time = input("Time: ").strip().upper()
counter = 0

with open("campeoes.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[0].strip().upper() == time:
            counter += 1

print(f"Títulos do Corinthians: {counter}")