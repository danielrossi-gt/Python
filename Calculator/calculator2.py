try:
    x = int(input("x: "))
except:
    print("x não é um número inteiro válido")
    exit()

try:
    y = int(input("y: "))
except:
    print("y não é um número inteiro válido")
    exit()

z = x / y

#Formatando para ter 50 casas de precisão no float
print(f"{z:.50f}")