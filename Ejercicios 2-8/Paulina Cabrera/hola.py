
listita= [11, 5, 8, 23, 6, 12, 24]

media = sum(listita)/len(listita)
print(media)

listita= [11, 5, 8, 23, 6, 12, 24]


def media(listita):
    media = sum(listita)/len(listita)
    return media

def varianza(listita):
    varian = 0
    for i in listita:
            varian+= (i - media(listita))**2
    varianza2= varian/len(listita)
    return varianza2

def desviancion_tipica(listita):
    desviacion = varianza(listita)**(0.5)
    return desviacion
print(media(listita))
print(varianza(listita))
print(desviancion_tipica(listita))



