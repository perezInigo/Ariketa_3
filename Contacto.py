class Contacto:
    izena = ""
    telefonoa = ""
    email = ""

    def __init__(self,i_izena,i_telefonoa,i_email):
        self.izena = i_izena
        self.telefonoa = i_telefonoa
        self.email = i_email

    def getter_izena(self):
        return self.izena

    def setter_izena(self,i_izena):
        self.izena = i_izena

    def getter_telefonoa(self):
        return self.telefonoa

    def setter_telefonoa(self,i_telefonoa):
        self.telefonoa = i_telefonoa

    def getter_email(self):
        return self.email

    def setter_email(self,i_email):
        self.email = i_email