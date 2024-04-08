def miFuncion():
    print('mi primera chamba')
    
#miFuncion()
    
#def imprimedato(nombre, apellido):
    #print('el nombre completo es', nombre, apellido)

#imprimedato('chancho', 'ql')            #el valor dentro de los parentesis de la funcion corresponde a un PARAMETRO, pero cuando referenciamos a ese valor dentro de la funcion se llama ARGUMENTO


#para cantidadd de argumentos variables:

def imprimedato(*nombre):
    print('el nombre completo es', nombre[0], nombre[1])

#imprimedato('chancho', 'culiao', 'de', 'mierda') 

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

#nombreCompleto(nombre='chancho', apellido='ql')
    
def nombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'], kwargs['pata'])

#nombreCompleto2(nombre='chancho', apellido='ql', pata='patita')

def miFuncion2(argumento = 'chancho'):
    print(argumento)

#miFuncion2('batman')
#miFuncion2()
    
def miFuncionLista(lista):
    for el in lista:
        print(el)

#miFuncionLista(['chancho', 'ql'])  #utilizamos parentesis de corchete ya que estamos definiendo una lista

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i
    
nombres = concatenaNombres(['aaaaaaaaaaa', 'aaadddddd'])
print(nombres)

def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(2) #recursividad sirve principalmente para una coleccion de datos o para hacer reintentos para llamr alguna base de datos si esta falla

def mifuncion4(apellidos):
    if apellidos == 'cordero':
        print('su apellido corresponde a los seleccionados para rendir el examen')

mifuncion4('cordero')
