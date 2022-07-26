#BUCLES

#1
repeticion = input('Decime una palabra')
for i in range(0,10):
    print (repeticion)

#2
valor = int (input("Ingrese un número positivo"))
i = 0
arr = []
while i < valor:
        i+= 1
        if(i % 2 != 0):
            arr.append(i)
print(arr)

# i = 0
# array = []
# while(i<10):
#     num = int(input('Decime un número entero positivo'))
#     if (num%2!=0):
#         array.append(num)
#     i +=1
# print(array)

# valor = int (input("Ingrese un número positivo"))
# i = 0
# while i < valor:
#         i+= 1
#         if(i % 2 != 0):
#             print(i)

# 2 v2
# num = int(input('Decime un número entero positivo'))
# num2 = 0
# while (num2 <= num):
#     num2 +=1
#     if num % 2 == 1:
#         print (num) 

# 2 v3
# num=int(input("Ingresa un numero entero: "))
# i=1
# if (type(num)==int) and num>1:
#     print("Los números impares hasta ",num," son:")
#     while i<=num:
#         if (i%2 != 0):
#             print(i, ",")
#         i+=1

# 2 v4
# valor = int (input("Ingrese un número positivo"))
# i = 0
# while i < valor:
#         i+= 1
#         if(i % 2 != 0):
#             print(i)

#3
num = int(input('Decime un número entero positivo'))
print ('Tabla de multiplicar del' , num)
for i in range(1,11):
    print(num , '*' , i , "=" , (num*i))

#4
contraseña = 'queso'
pregunta = input('Contraseña')
while(contraseña!=pregunta):
    pregunta=input('Intente nuevamente')
print('Accediendo')

#5
frase = input('Decime una frase')
letra = input('Decime una letra')

i=0
array = []
for L in frase:
    if (letra == L):
        array.append(L)
        letrasTotales = len(array)
    i+=1
print (letrasTotales)

