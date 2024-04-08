c = open('holamundo.txt', 'w')   #podemos añadir permisos a la lectura del archivo al igual que en bash (read, append, write, x <- para crear archivos)
#print(c.read())           #.read a c es una propiedad en la que a la variable definida leemos todo su contenido

#para leer linesa de 1 a 1 tenemos el codigo c.readline

#print(c.readline())
#print(c.readline())
#print(c.readline())

#for x in c:
    #print(x)  #llamamos a x ya que corresponde a cada una de las lineas que se encuentran dentro del arvhivo definido como c

#c.write('\nhola amiwos') #gracias al \n podemos indicar que el texto agregado correrá en otra linea

c.close()

#x = open('holamundo.txt')

#print(x.read())

import os 


if os.path.exists('holamundo.txt'):
    os.remove('holamundo.txt')
else:
    print('el archivo no existe')

os.rmdir('micarpeta')  #usamos practicamente los mismos comando quee n bash para crear y eliminar archivos y directorios

