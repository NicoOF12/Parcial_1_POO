"""Se crea una clase Alumno,
    que recibe como atributos
    Nombre y Nota"""


class Alumno():

    """Se define el constructor de la
        clase Alumno y se definen los atributos"""

    def __init__(self, Nombre, Nota):
        self._Nombre = Nombre
        self._Nota = Nota

    """Se define un método Obtener_Datos
        el cual sirve para que el usuario
        ingrese el Nombre y la Nota del alumno"""

    def Obtener_Datos(self):
        self._Nombre = input('Ingrese el Nombre del alumno: ')
        self._Nota = input('Ingrese la Nota del alumno: ')
        self._Nota = float(self._Nota)

    """Se define un método Resultado
        el cual tiene la funcionalidad
        de verificar si la nota ingresada
        es correcta y definir si el alumno
        ha aprobado o no ha aprobado"""

    def Resultado(self):
        if (self._Nota >= 0.0 and self._Nota <= 5.0):
            if (self._Nota >= 3.0 and self._Nota <= 5.0):
                print('El alumno', self._Nombre,
                      'con nota:', self._Nota, 'ha aprobado')
            elif (self._Nota >= 0.0 and self._Nota < 3.0):
                print('El alumno', self._Nombre, 'con nota:',
                      self._Nota, 'no ha aprobado')
        else:
            print('Ingrese una nota válida entre 0.0 y 5.0')


alumno = Alumno(" ", 0)
alumno.Obtener_Datos()
alumno.Resultado()
