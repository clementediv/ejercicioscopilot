#ESCRIBIR UNA FUNCION QUE RECIBA NOMBRE Y APELLIDO Y LOS VAYA AGREGANDO A UN ARCHIVO 

def NombreArchivo(nombre, apellido):
    c = open('nombrecompleto.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

NombreArchivo('Clemente', 'Uribe')

 