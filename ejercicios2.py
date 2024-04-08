#MULTIPLICAR DOS NÚMEROS SIN UTILIZAR EL SÍMBOLO DE MULTIPLICACION
a = 4
b = 8
resultado = 0

for x in range(a):
    resultado += b

print(resultado)

#INGRESE NOMBRE Y APELLIDO Y DEVUÉLVALE AL REVÉS 

nombre = 'Clemente'
apellido = 'Uribe'

concatenacion = nombre + ' ' + apellido

print(concatenacion[::-1])      #utilizando el comando [::-1] pordemos dar vuelta un string en python 

#ESCRIBIR UNA FUNCIÓN QUE ENCUENTRE EL ELEMENTO MENOR DE UNA LISTA

lista = [1, 2, 5, 55, 100, -24]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor 

print('menor', menor)

#ESCRIBIR UNA FUNCIÓN QUE DEVUELVA EL VOLUMEN DE UNA ESFERA POR SU RADIO
#4/3 * pi * r ** 3

def CalculaVolumen(r):
    return 4 / 3 * 3,1415 * r ** 3

resultado = CalculaVolumen(6)
#print(resultado)


radio = input('ingrese radio')

try:
    radio = int(radio)

except:
    radio = 'hola'   #este except solo necesita un = y no 2 == ya que necesitamos que lo introducido cumple el if solo is es un string y no si es una palabra en específico

if radio == 'hola':
    print('debe escribir el radio numericamente')
    exit()

else:
    print(4 / 3 * 3.14 * radio ** 3)


#ESCRIBIR UNA FUNCION QUE INDIQUE SI EL USUARIO ES MAYOR DE EDAD
    
    edad = input('ingrese su edad')

try:
    edad = int(edad)

except:
    edad = 'hola'

if edad == 'hola':
    print('debe ingresar su edad en números')
    exit()

elif edad < 18:
    print('el usuario no es mayor de edad')

elif edad >= 18:
    print('el usuario es mayor de edad por lo tanto tiene acceso a la computadora')

else:
    print(' ')

#ESCRIBIR UNA FUNCION QUE INDIQUE SI UN NUMERO ES PAR O IMPAR
    
def EsPar(n):
    return n % 2 == 0

resultado = EsPar(10)
print(resultado)

#ESCRIBIR UNA FUNCION QUE INDIQUE CUANTAS VOCALES TIENE UNA PALABRA

palabra = 'perroshikO'
vocales = 0

for  x in palabra:
    y = x.lower()
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0 #or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U' else 0

print(vocales)


#ESCRIBIR UNA APLICACION QUE ESCRIBA UNA CANTIDAD INFINITA DE NUMEROS HASTA DECIR BASTA, LUEGO QUE DEVUELVA LA SUMA DE LOS NUMEROS INGRESADOS 

lista = []
print('ingrese numeros y para salir escriba "basta"')
while True:
    valor = input('ingrese valor: ')
    if valor == 'basta':
        break
    else:
        try:
            valor = int(valor)   #la funcion int transforma un string a numero entero
            lista.append(valor)
        except:
            print('El dato ingresado no es válido')
            exit()

resultado = 0

for x in lista:
    resultado += x

print(resultado)

#ESCRIBIR UNA FUNCION QUE RECIBA NOMBRE Y APELLIDO Y LOS VAYA AGREGANDO A UN ARCHIVO 
#revisar ejercicios3.py

