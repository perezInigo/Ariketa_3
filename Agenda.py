from Contacto import Contacto

class Agenda:

    contactos = []
    def __init__(self,i_contactos):
        self.contactos = i_contactos

    def añadir(self):
        print("Inserte nombre: ")
        nuevo_nombre = input()
        print("Inserte telefono: ")
        nuevo_telefono = int(input())
        print("Inserte el nuevo email: ")
        nuevo_email = input()
        nuevo_ontacto = Contacto(nuevo_nombre,nuevo_telefono,nuevo_email)
        self.contactos.append(nuevo_ontacto)

    def lista(self):
        print("-------------USUARIOS-------------")
        for contacto in self.contactos:
            print(contacto.izena)

    def buscar(self,i_izena):
        for contacto in self.contactos:
            if(contacto.izena == i_izena):
                print("------------RESULTADO-------------")
                print("Nombre: " + contacto.getter_izena())
                print("Telefono: " + str(contacto.getter_telefonoa()))
                print("Email: " + contacto.getter_email())
                print("----------------------------------")

    def editar(self,i_izena):
        nuevo_telefono = 0
        for contacto in self.contactos:
            if (contacto.izena == i_izena):
                print("------------RESULTADO-------------")
                print("Nombre: " + contacto.getter_izena())
                print("Telefono: " + contacto.getter_telefonoa())
                print("Email: " + contacto.getter_email())
                print("----------------------------------")
                print("¿Que dato quieres cambiar al contacto?")
                campo = input()
                if campo.lower() == "nombre":
                    print("Inserte el nuevo nombre: ")
                    nuevo_nombre = input()
                    contacto.setter_izena(nuevo_nombre)
                    print("Se ha cambiado el nombre con exito!")
                if campo.lower() == "telefono":
                    while nuevo_telefono.length() != 9:
                        print("Inserte el nuevo telefono: ")
                        nuevo_telefono = int(input())
                    contacto.setter_telefonoa(nuevo_telefono)
                    print("Se ha cambiado el telefono con exito!")
                if campo.lower() == "email":
                    print("Inserte el nuevo email: ")
                    nuevo_email = input()
                    contacto.setter_email(nuevo_email)
                    print("Se ha cambiado el email con exito!")
                print("-------CAMBIOS REALIZADOS---------")
                print("Nombre: " + contacto.getter_izena())
                print("Telefono: " + contacto.getter_telefonoa())
                print("Email: " + contacto.getter_email())
                print("----------------------------------")