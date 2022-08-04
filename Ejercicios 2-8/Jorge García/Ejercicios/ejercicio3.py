# Escribir un programa que reciba una cadena de caracteres y 
# devuelva un diccionario con cada palabra que contiene y su frecuencia. 
# Escribir otra función que reciba el diccionario generado con la función anterior 
# y devuelva una tupla con la palabra más repetida y su frecuencia.

def calcularOcurrencias(texto):
    texto = texto.lower()
    ocurrencias = {}
    lista = texto.split(' ')
    for palabra in lista:
        ocurrencias[palabra] = ocurrencias.get(palabra, 0) + 1
    return ocurrencias

def guardarOcurrencias(dic_ocurrencias):
    max = 0
    palabra_max = ""
    for clave, valor in dic_ocurrencias.items():
        if(valor > max):
            max = valor
            palabra_max = clave
    return (palabra_max, max)


texto = "hola hola como como como como como estas estas estas"
dic_occurrencias = calcularOcurrencias(texto)
print(dic_occurrencias)
tupla_ocurrencias = guardarOcurrencias(dic_occurrencias)
print(f"Palabra que más se repite: {tupla_ocurrencias}")