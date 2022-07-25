clave = "pepe123"
claveIngresada = input("Ingrese la contraseña: ")

while clave != claveIngresada:
    claveIngresada = input("Incorrecta. Ingresa nuevamente: ")

print("¡Clave correcta!")