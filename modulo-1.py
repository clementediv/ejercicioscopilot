from modulos import saludo, edad, mascotas   #importando podemos acceder a todas las funciones y variables creadas en ese archivo/ el comando as renombra el modulo llamado a este archivo
from camelcase import CamelCase

print(mascotas)
saludo('Clemente')
edad(2003)

c = CamelCase()
s = 'esta oracion necesita CamelCase'

camelcased = c.hump(s)
print(camelcased)

