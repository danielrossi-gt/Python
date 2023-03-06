contatos = {
    "João" : "3546-5454",
    "José" : "3442-9875",
    "Maria" : "3546-8787"
}

nome = input("Digite o nome: ")

if nome in (contatos):
    numero = contatos[nome]
    print(numero)
    exit(0)

print("Nome não encontrado")    
exit(1)