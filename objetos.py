class Usuario:  #estamos creando una clase (el plano de un usuario) al lado de class va el nombre
    def __init__(self, nombre, apellido, altura):  #self es la instancia del usuario y a esta instancia se le agrega una propiedad luego del punto
        self.nombre = nombre
        self.apellido = apellido
        self.altura = altura
    
    def saludo(self):
        print('Hola!', 'mi nombre es', self.nombre, self.apellido, 'y mi estatura es de:', self.altura)
        


usuario = Usuario('Felipe', 'Feliz', '174cm')  #debemos llamar al usuario como si este fuera una funcion (), de esta manera el usuario correspondera a un objeto
usuario2 = Usuario('Chanchito', 'Feliz', '190cm')

#usuario.saludo()
#usuario.nombre = 'Perro'
#usuario.saludo()
#del usuario.nombre
#del usuario
#print(usuario)


#en resumen nuestras clases son el plano de lo que nosostros queremos crear, en el caso de los usuarios es el como se crean, y los objetos son instancias de estos planos, ej: el usuario ya existe
#__init__ se ejecuta siempre cuando nosotros creamos una instancia de estos usuarios, y self hace ref a una instancia, podemos cambiar los valores de dichas instancias, self no es necesario pasarlo como parametro, pero si necesitamos entregar los demas valores para generar la instancia de por si

#--------------------------HERENCIA--------------------------------

class Admin(Usuario):
    def superSaludo(self):
        print('Hola, me llamo', self.nombre, 'y soy administrador')


#admin = Admin('Super', 'Administrador', '200 cm')
#admin.saludo()
#admin.superSaludo()

#usuario.superSaludo() no corre ya que supersaludo es una instancia de la clase padre

#-------------------------------EJERCICIO-------------------------

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un', self.tipo, 'mi nombre es', self.nombre, 'y mi sonido es el', self.onomatopeya)


class Gato(Animal):    
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya) #en este caso llamamos al comportamiento de la clase padre para manternerlo de todas formas
        print('Hola soy un gato extendido')   #extendemos el comprtamiento del metodo init de la clase padre

gato = Gato('Waton', 'Maullido')

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('instanciando un perro piola')

perro = Perro('Perro shico', 'Ladrido')

class Canario(Animal):
    tipo = 'canario'

canario = Canario('Piolin', 'Silvido')

gato.saludo()
perro.saludo()
canario.saludo() 