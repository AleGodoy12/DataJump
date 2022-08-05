# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una datos 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

respuesta = 0
persona = {}
while respuesta != 1:
    dato = input("Ingresa el dato que quieres agregar: ")
    valor = input(f"Ingresa tu {dato}: ")
    persona[dato] = valor
    print(persona)
    respuesta = int(input("Si quieres salir ingresa [1], si no ingresa [2]: "))