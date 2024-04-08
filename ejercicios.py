#dato = input('Ingrese dato: ')

#lista = ('hola mundo', 'chancho', 'calabazas')

#f lista.count(dato) > 0: 
    #print('El dato existe', dato)

#else: 
    #print('el dato no existe :(', dato)

primero = input('Ingrese primer numero')

try:
    primero = int(primero)

except:
    primero = 'chancho ql'

if primero == 'chancho ql':
    print('el valor indicado no es un entero')
    exit()

segundo = input('Ingrese segundo numero')

try:
    segundo = int(segundo)

except:
    segundo = 'chancho ql'

if segundo == 'chancho ql':
    print('el valor indicado no es un entero')
    exit()

#if primero == 'chancho ql' or segundo == 'chancho ql':
    #print('ingresaste mal algun dato, prueba de nuevo solo con numeros')
#else:
simbolo = input('ingrese operación: ')
if simbolo == '+':
    print('suma', primero + segundo)

elif simbolo == '-':
    print('resta', primero - segundo)

elif simbolo == '*':
    print('multiplicacion', primero * segundo)

elif simbolo == '/':
    print('división', primero / segundo)

else:
    print('el simbolo ingresado no es válido')






#PrimerNumero = int(primero)           #con el comando int transformamos el string a número entero
#SegundoNumero = int(segundo)
#print(PrimerNumero + SegundoNumero)
