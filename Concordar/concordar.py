#resposta = input("Você concorda? ")
#Converte a resposta para maiúsculas para comparar
#if resposta.upper() == "S" or resposta.upper() == "SIM":
#    print("Você concordou.")
#elif resposta.upper() == "N" or resposta.upper() == "NÃO":
#    print("Você não concordou.")
#else:
#    print("Resposta Inválida.")

resposta = input("Você concorda? ").upper()

if resposta in ("S", "SIM"):
    print("Você concordou.")
elif resposta in ("N", "NÃO"):
    print("Você não concordou.")
else:
    print("Resposta Inválida.")
