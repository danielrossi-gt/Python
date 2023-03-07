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

#def get_value(time):
#    return times[time]

#for time in sorted(times):
#for time in sorted(times, reverse=True):
#for time in sorted(times, key=get_value, reverse=True):
for time in sorted(times, key=lambda time: times[time], reverse=True):
     print(time, times[time])
