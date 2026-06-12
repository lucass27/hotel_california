from funciones2 import *

def principal():
    while True:
        opciones_menu()
        opcion = ingresarOpcion()
        
        if opcion == 1:
            cantidad = int(input("¿Cuántas reservas desea registrar? "))
            for i in range(cantidad):
                id_habitacion = input("Ingrese el ID de la habitación: ")
                reservar_habitacion(id_habitacion)
                asignar_huesped(int(id_habitacion))
                asignar_noches(int(id_habitacion))
                asignar_servicio(int(id_habitacion))
                asignar_estado_reserva(int(id_habitacion))

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