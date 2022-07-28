# *Ejercicios Tipo de datos simples:*

# 1. Print "Hola mundo"

print("¡Hola Mundo!")

# 2. Hola mundo en una variable

saludo = "¡Hola Mundo!"
print(saludo)

#3. Horas trabajadas

horasTrabajadas = int(input("Cuantas horas trabajaste?"))
valorHoras = int(input("Cuanto vale tu hora de trabajo?"))
pagaTotal = horasTrabajadas * valorHoras

print("Te corresponde la siguiente paga: $" + str(pagaTotal) )

#4. Calculadora de masa corporal

peso = float(input("Ingrese su peso en kgs"))
altura = float(input("Ingrese su esatura en mts"))
masaCorporal = peso / pow(altura, 2)

print("Tu masa corporal es " + str(round(masaCorporal, 2)))


#5. Descuento en barras de pan 

costoPan = 3.49
descuento = 0.60

panViejo = int(input("Cuantas barras de pan que no son del día se vendieron?"))

formulaDescuento = ( costoPan * panViejo ) * descuento

descuentoAplicado = ( costoPan * panViejo ) - formulaDescuento

print("El precio habitual del pan es de €" + str(costoPan))
print("El descuento aplicado es de €" + str(formulaDescuento))
print("El precio final es de €" + str(descuentoAplicado))


# *Ejercicios condicionales*

#1. Mayor o menor de edad

edad = int(input("Ingrese su edad"))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


#2. Contraseñas

passSistema = "contraseña"
passIngresada = str(input("Ingrese su contraseña"))

if str.casefold(passIngresada) == passSistema:
    print("Puede ingresar")
else: 
    print("Contraseña incorrecta")


#3. Numero par y impar

ingreseNumero = int(input("Ingrese un número"))
moduloNum = ingreseNumero%2 

if moduloNum == 0:
    print("El número es par")
else:
    print("El número es impar")


#4.Entrada a la sala de juegos

ingreseEdad = int(input("Ingrese su edad"))

if ingreseEdad < 4:
    print("Entra gratis")
elif ingreseEdad >= 4 and ingreseEdad < 18:
    print("Debe abonar 5Є")
else:
    print("Debe abonar 10Є")


#5. Empieza con

abc1 = ("A", "B", "C", "D","E","F","G","H","I","J","K","L","M")
abc2 = ("N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
nombre = str(input("Ingrese su apellido"))
sexo = str(input("Ingrese sexo (masculino o femenino)"))

if nombre.startswith(abc1) and sexo == "femenino" or nombre.startswith(abc2) and sexo == "masculino":
    print ("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")



# *Ejercicios Bucles*

#1. Pide nombre al usuario y lo muestra 10 veces

nombre = str(input("Ingrese su nombre"))
x = 0

while x < 10:
    x += 1
    print(nombre)


#2. Números impartes

valor = int (input("Ingrese un número positivo"))
i = 0
arr = []
while i < valor:
        i+= 1
        if(i % 2 != 0):
            arr.append(i)
print(arr)


#3.Tabla de multiplicar del 1 al 10

multiplicando = int(input("Ingrese un número"))
multiplicador = 0

while multiplicador < 10:
    multiplicador += 1
    print(multiplicador * multiplicando)

#4. Preguntar por contraseña

contraseña = "contraseña"
ingreseContraseña = str(input("Ingrese su contrseña"))

while contraseña != ingreseContraseña:
    ingreseContraseña = str(input("Ingrese su contrseña"))
else:
    print("Bienvenidx")

#5. Contabilizador de letras

frase = str(input("Ingrese una frase"))
letra = str(input("Ingrese una letra"))
acumulador = 0


while acumulador < frase.count(letra):
      acumulador += 1

print(acumulador)
