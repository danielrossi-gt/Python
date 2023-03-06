try:
    x = int(input("x: "))
except:
    print("x não é um número inteiro válido")
    exit()

if x % 2 == 0:
    print("O número é par.")    
else:
    print("O número é impar")