from Contacto import Contacto

class Agenda:

    contactos = []
    def __init__(self,i_contactos):
        self.contactos = i_contactos

    def añadir(self,i_izena,i_telefonoa,i_email):
        nuevo_ontacto = Contacto(i_izena,i_telefonoa,i_email)
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
                print("Telefono: " + contacto.getter_telefonoa())
                print("Email: " + contacto.getter_email())
                print("----------------------------------")

    def editar(self):
        print("")