# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono 
# y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
# vive en <dirección> y su número de teléfono es <teléfono>.

nombre = input("Nombre: ").capitalize()
edad = int(input("Edad: "))
direccion = input("Dirección: ").capitalize()
telefono = input("Teléfono: ")

if(edad > 0 and edad < 100 and nombre.isalpha()):
    persona = {}
    persona['Nombre'] = nombre 
    persona['Edad'] = edad 
    persona['Direccion'] = direccion 
    persona['Telefono'] = telefono 
    print(f"{persona['Nombre']} tiene {persona['Edad']} años, vive en {persona['Direccion']} y su número de teléfono es {persona['Telefono']}")
else:
    print("Datos inválidos.")
