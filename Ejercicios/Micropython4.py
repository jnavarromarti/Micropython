# Micropython: NO.4
# Progrma que genera un número aleatorio entre 1 y 100 y el usuario debe adivinarlo en 8 intentos
from random import randint
valor_secreto = randint(1, 100)
print("Adivina el número secreto")
print(valor_secreto)
oportunidades = 8
for oportunidad in range(oportunidades):
    valor = int(input("Introduce un número entre 1 y 100: "))
    
    if valor > 100: 
        print("El número introducido es mayor que 100")
    elif valor < 1:
        print("El número introducido es menor que 1")
    elif valor > valor_secreto:
        print("El número secreto es menor")
    elif valor < valor_secreto:
        print("El número secreto es mayor")
    else:
        print("¡Has acertado!")
        break
    oportunidades -= 1
    print(f"Te quedan {oportunidades} oportunidades")
   
if oportunidades == 0:
    print(f"El número secreto era {valor_secreto}")
    print("¡Has perdido!")
