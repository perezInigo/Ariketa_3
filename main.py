from Contacto import Contacto
from Agenda import Agenda

Contacto1 = Contacto("Inigo","943005876","perez.inigo@uni.eus")
Contacto2 = Contacto("Unai","943005587","perez.unai@uni.eus")
Contacto3 = Contacto("Ander","943005123","perez.ander@uni.eus")
Contacto4 = Contacto("Gaizka","943005875","perez.gaizka@uni.eus")

Contactos = [Contacto1,Contacto2,Contacto3,Contacto4]

Agenda = Agenda(Contactos)

Agenda.lista()

Agenda.buscar("Inigo")

Agenda.añadir("Eneko","943558789","eneko.sdkf@gmail.com")
Agenda.lista()