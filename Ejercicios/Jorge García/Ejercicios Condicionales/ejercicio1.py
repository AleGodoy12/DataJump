from plistlib import InvalidFileException


edad = int(input("Ingresa tu edad: "))
edadMayor = 18
if (edad >= edadMayor):
    print("Eres mayor edad")
else:
    print("No eres mayor de edad")