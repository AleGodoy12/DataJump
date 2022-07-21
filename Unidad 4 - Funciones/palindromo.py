cadena1 = input("Dame la primera cadena: ")
cadena2 = input("Dame la segunda cadena: ")
print( cadena2[:2] + cadena1[2:] + " " + cadena1[:2] + cadena2[2:] )

cadena1 = input("Dame una cadena: ")
cadena_al_reves = cadena1[::-1]
print(cadena_al_reves)
if( cadena1 == cadena_al_reves ):
    print("Es palindromo")
else:
    print("No es palindromo")