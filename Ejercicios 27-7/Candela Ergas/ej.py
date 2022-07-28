def factorial():
    num= int(input("Ingresá un número positivo: "))
    i=0
    acum=1
    if num>0:
        while i<num:
            i+=1
            acum= acum*i
        print("El factorial de ",num," es: ",acum)
    else: 
        print("Error!El número debe ser positivo")

factorial()