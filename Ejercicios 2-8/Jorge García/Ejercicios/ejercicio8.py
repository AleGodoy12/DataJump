# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una datos 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

datos = {}

nombre = input("Nombre: ").capitalize()
datos['Nombre'] = nombre
print(datos)
edad = int(input("Edad: "))
datos['Edad'] = edad 
print(datos)
sexo = input("Sexo: ")
datos['Sexo'] = sexo 
print(datos)
direccion = input("Dirección: ").capitalize()
datos['Direccion'] = direccion 
print(datos)
telefono = input("Teléfono: ")
datos['Telefono'] = telefono 
print(datos)
mail = input("Correo electrónico: ")
datos['Mail'] = mail 
print(datos)
