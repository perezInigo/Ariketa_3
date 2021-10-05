from Contacto import Contacto
from Agenda import Agenda

Contacto1 = Contacto("Inigo","943005876","perez.inigo@uni.eus")
Contacto2 = Contacto("Unai","943005587","perez.unai@uni.eus")
Contacto3 = Contacto("Ander","943005123","perez.ander@uni.eus")
Contacto4 = Contacto("Gaizka","943005875","perez.gaizka@uni.eus")
Contactos = [Contacto1,Contacto2,Contacto3,Contacto4]
Agenda = Agenda(Contactos)

opcion = 0

while opcion != 5:
    print("----------Menú------------")
    print("1.- Añadir contacto.")
    print("2.- Lista de contactos.")
    print("3.- Buscar contactos.")
    print("4.- Editar contacto.")
    print("5.- Cerrar agenda.")
    print("--------------------------")
    print("Escribe el numero a ejecutar:")
    opcion = int(input())

    if opcion == 1:
        Agenda.añadir()
    if opcion == 2:
        Agenda.lista()
    if opcion == 3:
        print("Inserte el nombre de usuario que quieres buscar:")
        nombre_busqueda = input()
        Agenda.buscar(nombre_busqueda)
    if opcion == 4:
        print("Inserte el nombre de usuario que quieres editar:")
        nombre_editar = input()
        Agenda.editar(nombre_editar)