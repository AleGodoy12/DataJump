
contraseña = "queso"
i = 0
while(i<5):
    usuario = input('Contraseña')
    if(contraseña == usuario):
        return 'entraste'
    else:
        input('Intenta nuevamente')
    i+=1
