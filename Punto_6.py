"""Se crea la clase Banco
    que tendrá como atributos a tres objetos
    de la clase Cliente"""


class Banco:

    def __init__(self):
        self.cliente1 = Cliente("Nicolás",0)
        self.cliente2 = Cliente("Mónica",0)
        self.cliente3 = Cliente("Oscar",0)

    """Se define el método Operar
        que recibirá los clientes y 
        la operación a realizar"""

    def Operar(self):
        self.cliente1.Depositar(2750000)
        self.cliente2.Depositar(700000)
        self.cliente3.Depositar(680000)
        self.cliente3.Extraer(80000)
        self.cliente3.Mostrar_Total()

    """Se define el método Depósito_Total
        el cual se encarga de mostrar la Cantidad
        total de dinero que tiene el banco
        por sus clientes"""

    def Deposito_Total(self):
        Deposito_Total = self.cliente1._Cantidad + self.cliente2._Cantidad + self.cliente3._Cantidad
        print('El Banco tiene en su depósito un total de:', Deposito_Total)


"""Se crea la clase Cliente
    que recibirá como atributos el nombre
    y la cantidad de dinero del cliente"""


class Cliente:

    def __init__(self, Nombre, Cantidad):
        self._Nombre = Nombre
        self._Cantidad = Cantidad

    """Se define el método Depositar
        el cual tiene como funcionalidad
        ingresar dinero al Banco"""

    def Depositar(self, Cantidad):
        self._Cantidad = self._Cantidad + Cantidad

    """Se define el método Extraer
        el cual tiene como funcionalidad
        extraer dinero del Banco"""

    def Extraer(self, Cantidad):
        self._Cantidad = self._Cantidad - Cantidad

    """Se define el método Mostrar_Total
        que sirve para mostrar la cantidad total
        de dinero que un cliente tiene en
        el Banco"""

    def Mostrar_Total(self):
        print('El cliente', self._Nombre,'tiene depositado en el Banco:', self._Cantidad)


"""Se hacen los llamados respectivos para inicalizar
    la clase y sus métodos"""

banco1 = Banco()
banco1.Operar()
banco1.Deposito_Total()
