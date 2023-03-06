import sys

nomes = {"João", "José", "Maria", "Joana", "Carla"}

if "Joana" in nomes:
    print("Encontrou.")
    sys.exit(0)

print("Não encontrou.")
sys.exit(1)
