from funciones2_fase2 import *

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
                asignar_estado_provisorio(id_habitacion)

        elif opcion == 2:
            id_habitacion = input("Ingrese el ID de la habitación a eliminar: ")
            eliminar_reserva(id_habitacion)

        elif opcion == 3:
            id_habitacion = input("Ingrese el ID de la habitación a modificar: ")
            modificar_reserva(id_habitacion)

        elif opcion == 4:
            id_habitacion = input("Ingrese el ID de la habitación a confirmar: ")
            confirmar_reserva(id_habitacion)

        elif opcion == 5:
            print("1. Informe general de reservas")
            print("2. Reporte de ocupación")
            print("3. Reporte por categoría")
            sub = input("Ingrese una opción: ")
            while sub not in ["1","2","3"]:
                print(ROJO + "Opción no válida." + RESET)
                sub = input("Ingrese una opción: ")
            if sub == "1":
                informe_general()
            elif sub == "2":
                ocupacion()
            elif sub == "3":
                reporte_por_categoria()

        elif opcion == 6:
            print("1. Consultar estado de una habitación")
            print("2. Modificar categoría de habitación")
            print("3. Bloquear habitación por mantenimiento")
            print("4. Habilitar habitación bloqueada")
            print("5. Listar habitaciones por estado")
            print("6. Volver")
            sub = input("Ingrese una opción: ")
            while sub not in ["1","2","3","4","5","6"]:
                print(ROJO + "Opción no válida." + RESET)
                sub = input("Ingrese una opción: ")
            if sub == "1":
                id_habitacion = input("Ingrese el ID de la habitación: ")
                consultar_estado(id_habitacion)
            elif sub == "2":
                id_habitacion = input("Ingrese el ID de la habitación: ")
                modificar_categoria(id_habitacion)
            elif sub == "3":
                id_habitacion = input("Ingrese el ID de la habitación: ")
                bloquear_habitacion(id_habitacion)
            elif sub == "4":
                id_habitacion = input("Ingrese el ID de la habitación: ")
                habilitar_habitacion(id_habitacion)
            elif sub == "5":
                listar_habitaciones_por_estado()

        elif opcion == 7:
            print("Hasta luego!")
            break

principal()