# Escribir una función que calcule el máximo común divisor de dos números 
# y otra que calcule el mínimo común múltiplo.

def calcularMCD(num1, num2):
    if(num1 == num2):
        return num1
    numMayor = max(num1, num2)
    numMenor = min(num1, num2)
    resto = numMayor % numMenor
    if(resto == 0):
        return numMenor
    else:
        dividendo = numMenor
        divisor = resto
        resto = dividendo % divisor
        while resto != 0:
            dividendo = divisor
            divisor = resto
            resto = dividendo % divisor
        return divisor

def calcularMCM(num1, num2):
    resultado = num1*num2/calcularMCD(num1, num2)
    return resultado

resultado = calcularMCD(24, 75)
print("MCD =", resultado)

resultado = calcularMCM(180, 67)
print("MCM =", resultado)
