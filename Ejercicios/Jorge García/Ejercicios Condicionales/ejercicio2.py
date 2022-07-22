clave = "pepe123"
clave = clave.lower()
print(clave)
claveIngresada = input("Ingresa la contraseña: ")
#- Uso el lower para evaluar las contraseñas en minúsculas.
if(clave == claveIngresada.lower()):
    print("¡Clave correcta!")
else:
    print("Clave incorrecta. Inténtalo de nuevo más tarde.")