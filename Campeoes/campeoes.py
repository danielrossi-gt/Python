import csv

times = {
    "Corinthians" : 0,
    "Cruzeiro" : 0,
    "Flamengo" : 0,
    "Palmeiras" : 0,
    "São Paulo" : 0,
    "Fluminense" : 0,
    "Santos" : 0,
    "Atlético Mineiro" : 0
}

with open("campeoes.csv", "r") as campeoes:
    leitor = csv.reader(campeoes, delimiter=',')
    next(campeoes) #primeira linha é o título das colunas
    for linha in leitor:
        time = linha[0]
        #print(time)
        times[time] += 1

for time in times:
    titulos = times[time]
    print(f"{time} : {titulos}")
