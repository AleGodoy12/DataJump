peso = float(input("Ingresa tu peso (en kg): "))
altura = float(input("Ingresa tu altura (en metros): "))

imc = peso / altura
imc = round(imc, 2)
print("Te índice de masa corporal es: " + str(imc))