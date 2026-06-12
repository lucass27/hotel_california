from funciones2 import *

def principal():
    while True:
        opciones_menu()
        opcion = ingresarOpcion()
        
        if opcion == 1:
            cantidad = input("¿Cuántas reservas desea registrar? ")
            while not es_numero_positivo(cantidad):
                print("Cantidad inválida, ingrese un número positivo")
                cantidad = input("¿Cuántas reservas desea registrar? ")
            cantidad = int(cantidad)
            for i in range(cantidad):
                print("RESERVA N°: ", i+1)
                id_habitacion = input("Ingrese el ID de la habitación: ")
                id_habitacion = reservar_habitacion(id_habitacion)
                asignar_huesped(id_habitacion)
                asignar_noches(id_habitacion)
                asignar_servicio(id_habitacion)
                asignar_estado_reserva(id_habitacion)

        elif opcion == 2:
            id_habitacion = input("Ingrese el ID de la habitación a eliminar: ")
            eliminar_reserva(id_habitacion)

        elif opcion == 3:
            id_habitacion = input("Ingrese el ID de la habitación a modificar: ")
            modificar_reserva(id_habitacion)

        elif opcion == 4:
            informe_general()

        elif opcion == 5:
            print("Hasta luego!")
            break

principal()