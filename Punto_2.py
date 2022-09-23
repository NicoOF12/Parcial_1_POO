"""Se crea una clase llamada Persona
    la cual recibe como atributos
    Nombre y Edad"""


class Persona():

    """Se define el constructor de la
        clase Persona y se definen los atributos"""

    def __init__(self, Nombre, Edad):
        self._Nombre = Nombre
        self._Edad = Edad

    """Se define un método Digitar_Datos
        que sirve para que el usuario
        ingrese el Nombre y la Edad
        de una persona"""

    def Digitar_Datos(self):
        self._Nombre = input('Ingrese el nombre de la Persona: ')
        self._Edad = input('Ingrese la edad de la Persona: ')
        self._Edad = int(self._Edad)

    """Se define un método Mostrar_Datos
        el cual tiene como propósito
        mostrar los datos de la perona ingresada"""

    def Mostrar_Datos(self):
        print('El nombre de la Persona es:', self._Nombre)
        print('La edad de la Persona es:', self._Edad)

    """Se define un método Validar_Edad
        el cual sirve para verificar
        que la edad ingresada esté correcta
        y luego definir si la persona es
        mayor de edad o no lo es"""

    def Validar_Edad(self):
        if (self._Edad >= 0):
            if (self._Edad < 18):
                print(self._Nombre, 'aún es menor de edad')
            else:
                print(self._Nombre, 'es mayor de edad')
        else:
            print('Ingrese una edad válida')


persona = Persona(" ", 0)
persona.Digitar_Datos()
persona.Mostrar_Datos()
persona.Validar_Edad()
