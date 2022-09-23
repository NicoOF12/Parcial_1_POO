"""Se crea una clase Calculadora
    y recibe como atributos Valor1,
    Valor2 y Resultado"""

class Calculadora():

    """Se define el método constructor"""

    def __init__(self, Valor1, Valor2, Resultado):
        self._Valor1 = Valor1
        self._Valor2 = Valor2
        self._Resultado = Resultado

    """Se define un método Ingresar_Datos
        el cual sirve para ingresar los datos por teclado"""

    def Ingresar_Datos(self):
        self._Valor1 = input('Ingrese un Valor (Valor1): ')
        self._Valor1 = float(self._Valor1)
        self._Valor2 = input('Ingrese un Valor (Valor2): ')
        self._Valor2 = float(self._Valor2)

    """Se define un método Sumar_Datos
        que se usa para obtener el resultado
        de sumar los dos valores que el 
        usuario ha ingresado"""

    def Sumar_Datos(self):
        self._Resultado = (self._Valor1 + self._Valor2)
        print('La suma de los dos valores es:', self._Resultado)

    """Se define un método Restar_Datos
        que tiene como funcionalidad obtener
        el resultado de la resta de los valores
        ingresador por teclado"""

    def Restar_Datos(self):
        self._Resultado = (self._Valor1 - self._Valor2)
        print('La resta de los dos valores es:', self._Resultado)

    """Se define un método Multiplicar_Datos
        que sirve para obtener el resultado de
        la multiplicación de los dos valores"""

    def Multiplicar_Datos(self):
        self._Resultado = (self._Valor1 * self._Valor2)
        print('La multiplicación de los dos valores es:', self._Resultado)

    """Se define el método Dividir_Datos
        que tiene como finalidad obtener
        el resultado de la división de
        los dos valores ingresados"""

    def Dividir_Datos(self):
        self._Resultado = (self._Valor1 // self._Valor2)
        print('La división de los dos valores es:', self._Resultado)


calculadora = Calculadora(0, 0, 0)
calculadora.Ingresar_Datos()
calculadora.Sumar_Datos()
calculadora.Restar_Datos()
calculadora.Multiplicar_Datos()
calculadora.Dividir_Datos()
