#if 2 < 5:
    #print('2 es menor que 5')

#condiciones que podemos evaluar:
    # a == b igualdad (usaremos 2 signos iguales)
    # a < b una variable menor que la otra
    #a != b distintas
    #a <= b menor o igual

#if 2 == 2:
    #print('2 es igual a 2')
#if 2 ==3:
#    print('2 es igual a 3')

#if 2 > 5:
#    print('2 es mayor que 5')

#if 5 > 2:
#    print('5 es mayor a 2')

#if 2 != 3:
#    print('2 no es igual a 3')

#if 2 <= 3:
#    print('2 es menor o igual a 3')
    
if 2 > 3:
    print('lala')
elif 2 > 5:          #si la condicion anterior se evalua en falso corre la siguiente linea y evalua la condicion a la derecha de elif
    print('2 es menor a 5')
elif 2 < 5:
    print('2 es menor a 5 este es el segundo elfi')
else:
    print('yo me imprimo solo si todo lo enterior evalua en flaso')

if 2 > 3:
    print('lala')
else:
    print('hola grupo')

if 2 < 5: print('if de una linea') #if escrito de evaluacion rapida

print('cuando devuelve true') if 5 > 2 else print('cuando devuelve false') #operador ternario

if 2 < 5 and 3 > 2: #con and tenemos que ambas condiciones deben cumplirse
    print('2 es menor a 5 y 3 es mayor a 2')

if 2 > 4 or 4 <= 4:
    print('alguna de las condiciones era true')
