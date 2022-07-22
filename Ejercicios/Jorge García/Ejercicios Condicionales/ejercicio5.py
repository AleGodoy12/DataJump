# 5.- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres 
# con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte 
# al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Nombre: ").capitalize() #Para que la primera letra quede en mayúscula
sexo = input("Sexo [M o F]: ").upper()

if(nombre.isalpha and (sexo == "M" or sexo == "F")):
    primeraLetra = nombre[0]
    if(sexo == "F"):
        if(primeraLetra < "M"):
            print("Te toca el grupo A")
        else:
            print("Te toca el grupo B")
    else:
        if(primeraLetra > "N"):
            print("Te toca el grupo A")
        else:
            print("Te toca el grupo B")
else:
    print("Datos inválidos, inténtelo de nuevo.")
