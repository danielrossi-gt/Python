import csv

nome = input("Nome: ")
telefone = input("Telefone: ")

with open("contatos.csv", "a") as arqivo:
    gravar = csv.writer(arqivo)
    gravar.writerow([nome, telefone])
