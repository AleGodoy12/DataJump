#Plantear el siguiente enunciado en código: “Si es mayor de edad o está vacunado y tiene hijos que están vacunados, entonces puede viajar solo por tierra. Caso los hijos no estén vacunados, no puede viajar”

#Mayor de edad

esMayor = 12

# Vacunas

tieneVacunas = True

hijosVacunados = True

puedeViajar = (esMayor >= 18 or tieneVacunas) and hijosVacunados

if(puedeViajar == True):
    print("Puede viajar")
else: 
    print("No puede viajar") 