try:
    pontos = int(input("Quantos pontos você perdeu no primeiro exercício? "))
except:
    print("Valor informado não é um número inteiro válido")
    exit()

if pontos < 2:
    print("Você perdeu menos pontos que eu.")
elif pontos > 2:
    print("Você perdeu mais pontos que eu.")
else:
    print("Você perdeu o mesmo número de pontos que eu.")
