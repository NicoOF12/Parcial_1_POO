"""Se crea la clase Agenda"""


class Agenda:

    def __init__(self):
        self.contactos = []

    def Menu(self):

        opcion = 1

        while (opcion != 5):
            print('*** MENÚ ***')
            print('1. Añadir Contacto')
            print('2. Lista de Contactos')
            print('3. Buscar Contacto')
            print('4. Editar Contacto')
            print('5. Cerrar Agenda')

            opcion = int(input('Elija una opción: '))

            while (opcion < 1 or opcion > 5):
                opcion = int(
                    input(print('Elija una opción válida entre 1 y 5')))

            """Se crean una serie del if y elif
                que sirven para verificar la opción
                digitada por el usuario e ingresar a la función
                adecuada para realizar dicho comando"""

            if opcion == 1:
                self.Nuevo_Contacto()

            elif opcion == 2:
                self.Listar_Contactos()

            elif opcion == 3:
                self.Buscar_Contacto()

            elif opcion == 4:
                self.Editar_Contacto()

            elif opcion == 5:
                print('Cerrando Agenda... adiós')

    """Se define un método Nuevo_Contacto
        que tendrá como funcionalidad recibir
        el nombre, el teléfono y el email
        del contacto y lo convertirá en una cadena"""

    def Nuevo_Contacto(self):
        Nombre = input('Nombre: ')
        Telefono = input('Teléfono: ')
        Email = input('Email: ')
        self._Nombre = Nombre
        self._Telefono = Telefono
        self._Email = Email
        self.contactos.append({'Nombre': self._Nombre, 'Teléfono': self._Telefono, 'Email': self._Email})

    """Se define un método Listar_Contactos
        El cual recorre toda la lista de
        contactos y va mostrando en
        pantalla cada uno de los contactos
        con sus respectivos datos"""

    def Listar_Contactos(self):
        for contacto in self.contactos:
            print("##################################")
            print("Nombre:      ", contacto['Nombre'])
            print("Teléfono:    ", contacto['Teléfono'])
            print("Email:       ", contacto['Email'])

    """Se define un método Buscar_Contacto
        que ayudará al usuario a encontrar un
        contacto que esté contenido dentro de la
        agenda"""

    def Buscar_Contacto(self):
        Nombre = input('Ingrese el nombre a buscar: ')
        flag = 0
        for i in range(len(self.contactos)):
            if self.contactos[i]['Nombre'] == Nombre:
                contacto = self.contactos[i]
                print("Teléfono:    ", contacto['Teléfono'])
                print("Email:       ", contacto['Email'])
                return 
                
        print("El Nombre de contacto no está en la agenda...")
        return

    """Se define el método Editar_Contacto
        que le servirá al usuario para editar
        los datos de un contacto del que se tenga nueva
        información"""

    def Editar_Contacto(self):
        Nombre = input('Ingrese el nombre de contacto a editar: ')
        for i in range(len(self.contactos)):
            if self.contactos[i]['Nombre'] == Nombre:
                contacto = self.contactos[i]
                contacto['Nombre'] = input('Ingrese el Nombre: ')
                contacto['Telefono'] = input('Ingrese el Teléfono: ')
                contacto['Email'] = input('Ingrese el Email: ')
                return
            
        print("El Nombre de contacto no está en la agenda...")
        return

"""Se hacen los llamados respectivos para inicalizar
    la clase y sus métodos"""
agenda = Agenda()
agenda.Menu()
