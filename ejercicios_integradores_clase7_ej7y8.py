# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
# titular (que es una persona) y cantidad (puede tener decimales). 
# El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase: 
# Un constructor, donde los datos pueden estar vacíos. 
# Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero. 
# mostrar(): Muestra los datos de la cuenta. 
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa,
# no se hará nada. 
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
class Persona:
    def __init__(self, nombre = "", edad = 0):
        self.__nom = nombre
        self.__edad = edad
        
    @property
    def nombre(self):
        return self.__nom
    
    @nombre.setter
    def nombre(self, value):
        self.__nom = value

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, value):
        self.__edad = value

class Cuenta(Persona):
    def __init__(self, nombre="", edad=0, cantidad = 0):
         super().__init__(nombre, edad) 
         self.__titular = nombre
         self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, value):
        self.__titular = value
    
    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def set_cantidad(self, value):
        self.__cantidad = value

    def ingresar(self, cantidad):
            if cantidad <= 0:
                 pass
            else:
                self.__cantidad = self.__cantidad + cantidad
    
    def retirar(self, cantidad):
            self.__cantidad = self.__cantidad - cantidad
    
    def mostrar(self):
        print("El titular de la cuenta es:" , self.__titular, "\nEl monto de la cuenta es de: " , self.__cantidad)
    

c1= Cuenta()
c1.titular = "Maria"
c1.ingresar(1000) 
c1.retirar(400)
c1.mostrar() 

# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que 
# deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la 
# cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los 
# siguientes métodos para la clase: 
# - Un constructor. Los setters y getters para el nuevo atributo. 
# - En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay 
# que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero 
# menor de 25 años y falso en caso contrario.  Además, la retirada de dinero sólo se podrá hacer si el 
# titular es válido. 
# - El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

class CuentaJoven(Cuenta):
    def __init__(self, nombre="", edad= 0, cantidad=0, bonif = 0):
         super().__init__(nombre, edad, cantidad)
         self.__bonif = bonif

    @property
    def bonif(self):
        return self.__bonif
    @bonif.setter
    def bonif(self, value):
         self.__bonif = value
        
    @property
    def edad(self):
         return self.__edad
    @edad.setter
    def edad(self, value):
        self.__edad = value

    def es_titular_valido(self):
         if self.__edad >= 18 and self.__edad <25:
              return True
         else:
              return False
         
    def retirar(self, cantidad):
         res = self.es_titular_valido()
         if res == True:
            return super().retirar(cantidad)
         else:
              pass
    def mostrar(self):
         super().mostrar() 
         print("Cuenta Joven. La bonificacion es de: ", self.__bonif, "%.")
    

c2 = CuentaJoven()
c2.titular = "Ana"
c2.edad = 22
c2.bonif = 0.1
c2.ingresar(1000)
c2.retirar(200)
c2.mostrar()


