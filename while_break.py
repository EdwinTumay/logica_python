import random

meta = 20
caracol_1 = 0
caracol_2 = 0

while True:
    avance_caracol_1 = random.randint(1,4)
    avance_caracol_2 = random.randint(1,4)

    caracol_1 += avance_caracol_1
    caracol_2 += avance_caracol_2

    print(f"El caracol 1 avanza {avance_caracol_1} para un total de {caracol_1}")
    print(f"El caracol 1 avanza {avance_caracol_2} para un total de {caracol_2}")
    print(f"---------------------------------")

    if caracol_1 >= 20 or caracol_2 >= 20:
        break

if caracol_1 > caracol_2:
    print("El caracol 1 ha ganado")
elif caracol_2 > caracol_1:
    print("El caracol 2 ha ganado")
else:
    print("Esto es un empate")