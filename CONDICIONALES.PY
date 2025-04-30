'''
hacer un algoritmo en el cual proporcione 
el divisor y tiene que darme como resultado si 
multiplo o no de ese numero
================================
entrada ::> numero a evaluar
divisor ::> numero de divisor

num = int(input("Ingrese Numero: "))
div = int(input("Ingrese Divisor: "))

if (num % div == 0) :
    print("El Numero ",num, "Es multiplo de ",div)
else:
    print("El Numero ",num,"NO es Multiplo de", div)

#ejercicios de masa corporal
'''
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")

totpacientes = 0
cBajoPeso = 0
cPesoNormal = 0
cSobrePeso = 0
cObesidad = 0
while totpacientes<5:
    totpacientes = totpacientes + 1 
    print("---------------")
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    imc = peso / (altura ** 2)
    if imc < 18.5:
        cBajoPeso = cBajoPeso + 1
    elif 18.5 <= imc < 24.9:
        cPesoNormal = cPesoNormal + 1
    elif 25 <= imc < 29.9:
        cSobrePeso = cSobrePeso + 1
    else:
        cObesidad = cObesidad + 1
    
print("Pacientes Bajo de Peso : ",cBajoPeso)
print("Pacientes Peso Normal : ",cPesoNormal)
print("Pacientes Con SobrePeso : ",cSobrePeso)
print("Pacientes Con Obesidad : ",cObesidad)

totpacientes = 0
cBajoPeso = 0
cPesoNormal = 0
cSobrePeso = 0
cObesidad = 0
cPesoNormal = 0
def calcularimc(pesoh,alturah,cBajoPeso,cPesoNormal,cSobrePeso,cObesidad):
    imc = pesoh / (alturah ** 2)
    if imc < 18.5:
        cBajoPeso = cBajoPeso + 1
    elif 18.5 <= imc < 24.9:
        cPesoNormal = cPesoNormal + 1
    elif 25 <= imc < 29.9:
        cSobrePeso = cSobrePeso + 1
    else:
        cObesidad = cObesidad + 1
print("hola a todos")        


while totpacientes<5:
    totpacientes = totpacientes + 1 
    print("---------------")
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    calcularimc(peso,altura,cBajoPeso,cPesoNormal,cSobrePeso,cObesidad)
    
print("Pacientes Bajo de Peso : ",cBajoPeso)
print("Pacientes Peso Normal : ",cPesoNormal)
print("Pacientes Con SobrePeso : ",cSobrePeso)
print("Pacientes Con Obesidad : ",cObesidad)

print("=====================modificacion de la rama rubi ruiz======================")

x=9
y=10

def sumanumero(x,y):
    return x + y