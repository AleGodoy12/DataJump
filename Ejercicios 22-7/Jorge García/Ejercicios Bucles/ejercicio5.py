# 5.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase

frase = input("Frase: ")
letraBuscada = input("Letra: ")
contador = 0
for letra in frase:
    if(letra == letraBuscada):
        contador += 1
print("Cantidad de veces que aparece la letra '" + letraBuscada + "' en la frase '" + frase + "': " + str(contador))