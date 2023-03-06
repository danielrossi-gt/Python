from sys import argv, exit

if len(argv) != 2:
    print("Nome não informado.")
    exit(1) #Sai e retorna código de erro

print(f"Hello, {argv[1]}")
exit(0) #Sai e retorna código de sucesso