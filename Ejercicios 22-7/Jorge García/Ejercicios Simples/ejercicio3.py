horasTrabajadas = float(input("Ingresa las horas que trabajaste: "))
costePorHora = float(input("Ingresa el coste de trabajo por hora: "))

paga = horasTrabajadas * costePorHora
print("Te corresponden " + str(paga) + "$ pesos")