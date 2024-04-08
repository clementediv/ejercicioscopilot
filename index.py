if 3 > 5:
    print('esto no se va a imprimir')

x = 5
y = 'chancho feo'
#print (x, y)

correo = 'clemente.uribe.ortiz@gmail.com'

print(correo)


_mi_var = 'chanchoculio'
miVar = 'chanchoculiao'

a, b, c = 'lala', 'lele', 'lili'
#print(a, b, c)

valor1 = valor2 = valor3 = 'Chancho culiao'

#print(valor1, valor2, valor3)

inicio = 'Hola'
final = 'Mundo'

palabra = 'Hola mundo' #string
palabra1 = "hola mundo" #string

entero = 20  #entero
conDecimal = 20.2 #float
complejo = 1j

#print(palabra, palabra1, entero, conDecimal, complejo)

lista = ['zapato', 'pie', 'una']
lista2 = lista.copy()
lista.append('Zapato gigante') #.append a una lista le agrega elementos
#lista.clear()

#print(lista, lista2.count(1))
#print(len(lista), len(lista2)) #len permite contar elementos de una lista
LargoLista = len(lista)
LargoLista2 = len(lista2)

#print(LargoLista, LargoLista2)

#print(lista[1])  #este comando muestra el elemento de la lista ubicado en el segundo elemento

#lista.pop() #este comando elimina el último elemento de una lista
#lista.pop() #con este eliminaríamos el siguiente y así sucesivamente

#lista.remove('zapato') #elimina un string por separado

lista.reverse() #reverse the list
lista.sort()  #ordena los elementos de una lista, separados index de string (palabras de números)
#print(lista) 

tupla111 = ['hola', 'mundo', 'somos', 'tupla']
nueva_lista = list(reversed(tupla111))
#print(nueva_lista)

#lista/tupla.count('algo') cuenta los elementos de una lista/tupla
#lista/tupla.inex('algo') me dice en que índice se encuentra ese elemento de la lista/tupla

rango = range(7)
#print(rango)

diccionario = {
    "nombre": "waton",
    "raza": "persa",
    "edad": 5
}
#print(diccionario)
#print(diccionario['nombre']) #ambas formas de acceder a un solo valor dentro del diccionario, print(diccionario['valor']) ó print(diccionario.get('valor'))
#print(diccionario.get('nombre'))

diccionario['nombre'] = 'Fluffy' #modifica una propiedad del diccionario
#print(diccionario)
#print(len(diccionario)) #len cuenta elementos

diccionario['ronrronea'] = 'si' #añade un valor al diccionario


#diccionario.pop('ronrronea') #generalmente el .pop para un diccionario, una tupla o una lista elimina algun valor del mismo 

#diccionario.popitem() #elimina el úilimo valor de un diccionario

Copia_gato = diccionario.copy() #copia el diccionario, otra manera de hacerlo es con: nombre_de_la_variable = dict(diccionario)

#del diccionario['ronrronea'] elimina un valor específico del diccionario

diccionario.clear() #elimina todos los valores dentro del diccionario
#print(Copia_gato, diccionario)

#gatitos = {
#    "Fluffy":{
#    "nombre": "fluffy",
#   "edad": 4
#   },
#   "Mamba":{
#       "nombre": "black mamba",    todo esto es para hacer un diccionario con más diccionarios dentro, abajo tenemos otra manerad alternativa de hacerlo
#       "edad": 4
#    }
#}

fluffy = {
    "nombre": "fluffy",
    "edad": 4
}

mamba = {
    "nombre": "mamba",
    "edad": 6
}
gatitos = {
    "Fluffy": fluffy,
    "Mamba": mamba
}
print(gatitos)

perritos = dict(nombre="Puppy", edad=5, ladra="si") #con esto creamos un diccionario usando el constructor.dict esto nos permite añadir valores 1 a 1
print(perritos)
 

 #TIPOS DE DATOS BOOLEANOS:

verdadero = True
falso = False

print(verdadero)
print(falso)
