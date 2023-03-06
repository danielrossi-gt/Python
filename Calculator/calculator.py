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

print(x + y)