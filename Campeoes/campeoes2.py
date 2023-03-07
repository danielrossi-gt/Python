import csv

times = {}

with open("campeoes.csv", "r") as file:
    #reader = csv.DictReader(file) #resolver encoding do arquivo
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        #print(row['ano']) #resolver encoding do arquivo
        #print(row[0])
        time = row[0].strip().upper()
        if not time in times:
            times[time] = 0 
        times[time] += 1

#times.sort()

for time in sorted(times):
    print(time, times[time])
