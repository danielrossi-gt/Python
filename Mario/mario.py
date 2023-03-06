#Constroe colunas do jogo Mario
def main():
    altura = pegar_altura()
    for i in range(altura):
        print("#")   

    #faz a saída sem quebrar linha, escrevendo quatro ?
    print("?" * 4, end="") #default do parametro end é "\n" 
    print()
    print()

    for i in range(3):
        print("#" * 3)
    
def pegar_altura():
    while True:
        try:
            n = int(input("Altura: "))
            if n > 0:
                break
        except ValueError:
            print("Não é um número inteiro")
    return n

main()
