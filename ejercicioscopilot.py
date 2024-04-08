#CONVERSOR DE TEMPERATURA

def celcius_a_kelvin(temperatura):
    return temperatura - 273

resultado = celcius_a_kelvin(4)
print(resultado)   


def farenheith_a_celcius(temperatura):
    return (temperatura - 32) * 5 / 9

resultado = farenheith_a_celcius(1)
print(resultado)  

def kelvin_a_farenheith(temperatura):
    return (temperatura - 273) * 5 / 9 + 32

resultado = kelvin_a_farenheith(-3)
print(resultado)

#GESTOR DE CONTACTOS Gestor de Contactos: Crea una clase que represente un contacto con atributos como nombre, apellido, 
#número de teléfono y correo electrónico. Luego, implementa una clase que gestione una lista de estos contactos con funciones 
#para agregar, eliminar y buscar contactos.

class Contacto:
    def __init__(self, nombre, apellido, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

class Agenda:
    def __init__(self):
        self.contactos = []
    
    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
    
    def eliminar_contacto(self, nombre, apellido):
        self.contactos = [contacto for contacto in self.contactos if contacto.nombre != nombre or contacto.apellido != apellido]

    def buscar_contacto(self, nombre, apellido):
        return next((contacto for contacto in self.contactos if contacto.nombre == nombre and contacto.apellido == apellido), None)

agenda = Agenda()
contacto = Contacto('Juan', 'Perez', 129912931239, 'jp1090@gmail.com')
agenda.agregar_contacto(contacto)
print(agenda.buscar_contacto('Juan', 'Perez').email)
agenda.eliminar_contacto('Juan', 'Perez')



#CAJERO AUTOMÁTICO VIRTUAL: CREA UNA CLASE LLAMADA CUENTABANCARIA 
#QUE PERMITA A UN USUARIO DEPOSITAR, RETIRAR Y VER EL SALDO DE SU CUENTA. IMPLEMENTA MÉTODOS 
#COMO DEPOSITAR(), RETIRAR() Y VER_SALDO().


class Acciones:
    def __init__(self, dinero):
       self.dinero = dinero
    
    def ver_saldo(self):
        print('Usted posee', self.dinero, 'en su cuenta')
    
    def retirar(self, cantidad):
        if cantidad <= self.dinero:
            self.dinero -= cantidad
            print('usted ha retirado', cantidad , 'en su cuenta')
        else:
            print('Fondos insuficientes')

    def deposito(self, cantidad):
        self.dinero += cantidad
        print('Usted depositó', cantidad, 'en su cuenta')

    def giro(self, cantidad, receptor):
        if cantidad <= self.dinero:
            self.dinero -= cantidad
            receptor.dinero += cantidad  
            print('Usted ha girado', cantidad, 'a la cuenta de', receptor.nombre, receptor.apellido)
        else:
            print('fondos insuficientes')


class Usuarios(Acciones):
    def __init__(self, dinero, nombre, apellido):
        super().__init__(dinero) #La línea super().__init__(dinero) en el código de Python se utiliza para llamar al método constructor __init__ de la clase padre, que en este caso es Acciones. Al usar super(), estás asegurándote de que la clase Usuario herede correctamente todas las propiedades y métodos de la clase Acciones.
        self.nombre = nombre
        self.apellido = apellido



diego = Usuarios(1000, 'Diego', 'Velazquez')
esteban = Usuarios(1111111, 'Esteban', 'Uribe')
marcos = Usuarios(100, 'Marcos', 'Ortiz')



diego.ver_saldo()
esteban.retirar(0)
marcos.giro(100, esteban)
marcos.ver_saldo()    


      

#Sistema de Biblioteca: Diseña un sistema que gestione libros en una biblioteca. Crea clases para Libro, 
#Biblioteca y Usuario. Permite que los usuarios puedan “prestar” y “devolver” 
#libros, y que la biblioteca mantenga el registro de los libros disponibles y prestados.



#Juego de Adivinar el Número: Escribe un programa que seleccione un número aleatorio y permita al usuario adivinarlo. 
#El programa debe dar pistas si el número ingresado es mayor o menor que el número secreto y contar el número de intentos.
import random

print('Bienvenido al juego de adivinar el numero secreto: pista dicho numero es mayor a 0 y menor a 100, además solo se permiten numeros enteros, suerte')

numero_secreto = random.randint(1, 1)
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


#control+c detiene el programa XD


#Gestor de Tareas: Desarrolla una aplicación de línea de comandos para gestionar tareas pendientes. 
#Utiliza una lista para almacenar las tareas y permite al usuario agregar, eliminar, y ver tareas.
# Estructura de datos para almacenar tareas, la palabra def no es necesaria que vaya ligada a una clase...



tareas = []

# Funciones para operaciones de tareas
def agregar_tarea(tareas, titulo):
    tareas.append({'titulo': titulo, 'completada': False})

def eliminar_tarea(tareas, indice):
    if 0 <= indice < len(tareas):
        del tareas[indice]
    else:
        print("Índice no válido.")

def mostrar_tareas(tareas):
    for indice, tarea in enumerate(tareas):
        estado = 'Completada' if tarea['completada'] else 'Pendiente'
        print(f"{indice}. {tarea['titulo']} - {estado}")

def completar_tarea(tareas, indice):
    if 0 <= indice < len(tareas):
        tareas[indice]['completada'] = True
    else:
        print("Índice no válido.")

# Bucle principal del programa
while True:
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Completar tarea")
    print("5. Salir")
    
    eleccion = input("Ingrese su elección: ")
    
    if eleccion == '1':
        titulo = input("Ingrese el título de la tarea: ")
        agregar_tarea(tareas, titulo)

    elif eleccion == '2':
        try:
            indice = int(input("Ingrese el índice de la tarea a eliminar: "))
            eliminar_tarea(tareas, indice)
        except ValueError:
            print("Por favor, ingrese un número entero.")

    elif eleccion == '3':
        mostrar_tareas(tareas)

    elif eleccion == '4':
        try:
            indice = int(input("Ingrese el índice de la tarea a completar: "))
            completar_tarea(tareas, indice)
        except ValueError:
            print("Por favor, ingrese un número entero.")

    elif eleccion == '5':
        print("¡Hasta luego!")
        break

    else:
        print("Elección no válida, intente de nuevo.")


#Calculadora de Interés Compuesto:

print('Bienvenido a la calculadora de interes compuesto :)')

monto = input('Ingrese el capital que usted posee')

try:
    monto = int(monto)
except:
    monto = 'palabra'

if monto == 'palabra':
    print('debe ingresar un numero entero')
    exit()


interes = input('Ingrese el interes al cual esta asociado el calculo')

try:
    interes = float(interes)
except:
    interes = 'palabra'

if interes == 'palabra':
    print('debe ingresar un numero entero')
    exit()


tiempo = input('ingrese el periodo de capitalizacion en años')

try:
    tiempo = int(tiempo)
except:
    tiempo = 'palabra'

if tiempo == 'palabra':
    print('debe ingresar un numero entero')
    exit()


n = input('Ingrese el numero de veces que su dinero se capitaliza durante un año')

try:
    n = int(n)
except:
    n = 'palabra'

if n == 'palabra':
    print('debe ingresar un numero entero')
    exit()


print('este es el dinero con el que resultará luego de dicho periodo: ', monto *(1 + interes / n)** (tiempo * n))



#Generador de Contraseñas: Escribe un programa que genere contraseñas aleatorias para el usuario.
#Asegúrate de que las contraseñas generadas contengan una mezcla de letras mayúsculas, minúsculas, números y símbolos.

import random
import string

def generate_random_psswrd(length):
    # Genera una palabra aleatoria con la longitud especificada
    characters = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Ejemplo de uso: Generar una palabra aleatoria de longitud 8
random_word = generate_random_psswrd(10)
print(f"Contraseña: {random_word}", random.randint(100, 40000), sep='0')  #el comando sep=' ' indica la separacion entre cada input del print



#Juego de Piedra, Papel o Tijera: Implementa el clásico juego de piedra, papel o tijera donde el usuario puede jugar contra la compu
# El programa debe mostrar el resultado de cada ronda y llevar la cuenta del puntaje.

print('Bienvenido al juego de pierdra, papel o tijera')

jugador = input('Ingrese su elección: ')

opciones = ['tijera', 'papel', 'piedra']

eleccion_del_computador = random.choice(opciones)
print('la computadora eligió:', eleccion_del_computador)

if jugador == 'tijera' and eleccion_del_computador == 'tijera':
    print('usted ha empatado con la computadora')
elif jugador == 'tijera' and eleccion_del_computador == 'piedra':
    print('usted ha perdido')
elif jugador == 'tijera' and eleccion_del_computador == 'papel':
    print('usted ha ganado')
elif jugador == 'piedra' and eleccion_del_computador == 'piedra':
    print('usted ha empatado con la computadora')
elif jugador == 'piedra' and eleccion_del_computador == 'papel':
    print('usted ha perdido')
elif jugador == 'piedra' and eleccion_del_computador == 'tijera':
    print('usted ha ganado')
elif jugador == 'papel' and eleccion_del_computador == 'papel':
    print('usted ha empatado con la computadora')
elif jugador == 'papel' and eleccion_del_computador == 'tijera':
    print('usted ha perdido')
elif jugador == 'papel' and eleccion_del_computador == 'piedra':
    print('usted ha ganado')





#Analizador de Texto: Escribe un programa que analice un texto proporcionado por el usuario y proporcione 
#estadísticas como el número de palabras, el número de letras, la palabra más común y la letra más común.

texto = input('ingrese texto: ')


#Simulador de Dados: Programa un simulador de lanzamiento de dados que permita al usuario especificar el número de dados y 
#el número de caras de los dados, y luego muestre el resultado de cada lanzamiento.

#HACER UN GENERADOR DE SUDOKU :::::::::::::::

#TYPING GAME ............

#add a hardware code proggraming project using arduino or any of this staff