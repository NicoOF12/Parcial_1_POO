"""Se crea la clase Banco
    que tendrá como atributos
    Titular y Cantidad"""


class Cuenta:

    def __init__(self, Titular, Cantidad):
        self._Titular = Titular
        self._Cantidad = Cantidad

    """Se define el método Imprimir_Datos
        que tendrá como funcionalidad
        imprimir los datos de los clientes"""

    def Imprimir_Datos(self):
        print("Titular: ", self._Titular)
        print("Cantidad: ", self._Cantidad)


"""Se crea la clase CajaAhorro
    que tendrá como atributos
    Titular y Cantidad heredados
    de la clase Cuenta"""


class CajaAhorro(Cuenta):

    def __init__(self, Titular, Cantidad):
        super().__init__(Titular, Cantidad)

    """Se define el método Imprimir_Datos
        que hereda de la clase Cuenta dicho
        método y sirve para imprimir
        los datos del titular de
        la caja de ahorros"""

    def Imprimir_Datos(self):
        print('############################')
        print("Cuenta de Caja de Ahorros: ")
        super().Imprimir_Datos()


"""Se crea la clase PlazoFijo
    que recibe como atributos Titular,
    Cantidad, Plazo e Interes, de los cuales
    Titular y Cantidad son heredados de la 
    clase Cuenta"""


class PlazoFijo(Cuenta):

    def __init__(self, Titular, Cantidad, Plazo, Interes):
        super().__init__(Titular, Cantidad)
        self._Plazo = Plazo
        self._Interes = Interes

    """Se define un método Importe
        que imprimirá el valor total
        de interés ganado"""

    def Importe(self):
        self.Importe = self._Cantidad * self._Interes/100
        print("El total de interés: ", self.Importe)

    """Se define un mpetodo Imprimir_Datos
        que tiene como funcionalidad
        imprimir los datos del titular
        de la clase PlazoFijo,
        heredando el llamado Imprimir_Datos
        de la clase Cuenta, además imprime
        el plazo y el interés al que se accedió"""

    def Imprimir_Datos(self):
        print('#######################')
        print("Cuenta a Plazo fijo: ")
        super().Imprimir_Datos()
        print("Plazo: ", self._Plazo, "días")
        print("Interés: ", self._Interes, "%")
        self.Importe()


"""Se hacen los llamados respectivos para inicalizar
    la clase y sus métodos"""

caja1 = CajaAhorro("Nicolás", 2750000)
caja1.Imprimir_Datos()

plazo1 = PlazoFijo("Mónica", 600000, 90, 2)
plazo1.Imprimir_Datos()
