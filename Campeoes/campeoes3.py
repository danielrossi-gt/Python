import csv
import re

counter = 0

with open("campeoes.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        time = row[0].strip().upper()
        #if time == "CORINTHIANS":
        if re.search("^(CORINTHIANS|O.CORINTHIANS|A.CORINTHIANS)$", time):
            counter += 1

print(f"Títulos do Corinthians: {counter}")