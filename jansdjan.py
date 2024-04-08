import random

print('Bienvenido al juego de adivinar el numero secreto: pista dicho numero es mayor a 0 y menor a 100, además solo se permiten numeros enteros, suerte')

numero_secreto = random.randint(1, 100)
numero = 'numero'

while numero != numero_secreto:

    try:
        numero = input('Ingrese su número')
        numero = int(numero)
    
    
    except:
        numero = 'palabra'
    if numero == 'palabra':
        print('debe ingresar un entero')
        continue
    elif numero == numero_secreto:
        print('Ha adivinado el número secreto')
        break
    elif numero < numero_secreto:
        print('el número secreto es mayor jiji, siga intentando')
        continue
    elif numero > numero_secreto:
        print('el número secreto es menor jiji') 
        continue