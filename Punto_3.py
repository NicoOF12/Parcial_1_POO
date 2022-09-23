"""Se crea la clase Triangulo
    la cual recibe como atributos
    Lado1, Lado2 y Lado3"""

class Triangulo():

    """Se define el constructor de la
        clase Triángulo y se definen los atributos"""

    def __init__(self, Lado1, Lado2, Lado3):
        self._Lado1 = Lado1
        self._Lado2 = Lado2
        self._Lado3 = Lado3

    """Se define el método Ingresar_Lados
        que sirve para que el usuario digite
        los valores de los lados"""

    def Ingresar_Lados(self):
        self._Lado1 = input('Ingrese el primer lado del Triángulo: ')
        self._Lado1 = float(self._Lado1)
        self._Lado2 = input('Ingrese el segundo lado del triángulo: ')
        self._Lado2 = float(self._Lado2)
        self._Lado3 = input('Ingrese el tercer lado del triángulo: ')
        self._Lado3 = float(self._Lado3)

    """Se define un método denominado Lado_Mayor
        El cual tendrá una variable M en la que
        se guardará el valor mayor de los lados
        luego de verificar el valor mayor por medio
        de condicionales"""

    def Lado_Mayor(self):

        self._M = 0.0

        if (self._Lado1 >= self._M):
            self._M = self._Lado1

        elif (self._Lado2 >= self._M):
            self._M = self._Lado2

        elif (self._Lado3 >= self._M):
            self._M = self._Lado3

        print('El valor del lado con mayor tamaño es: ', self._M)

    """Se define el método Tipo_Triángulo
        que tendrá como funcionalidad definir el tipo
        de triángulo que es según la medida de cada
        uno de sus lados (Equilátero, Isósceles o Escaleno)"""

    def Tipo_Triangulo(self):

        if (self._Lado1 == self._Lado2 and self._Lado2 == self._Lado3):
            print('El Triángulo es Equilátero...\n')

        if (self._Lado1 == self._Lado2 and self._Lado1 != self._Lado3 or
                self._Lado1 != self._Lado2 and self._Lado1 == self._Lado3 or
                self._Lado1 != self._Lado2 and self._Lado2 == self._Lado3):
            print('El Triángulo es Isósceles...')

        if (self._Lado1 != self._Lado2 and self._Lado1 != self._Lado3 and
                self._Lado2 != self._Lado3):
            print('El Triángulo es Escaleno...')


triangulo = Triangulo(0, 0, 0)
triangulo.Ingresar_Lados()
triangulo.Lado_Mayor()
triangulo.Tipo_Triangulo()
