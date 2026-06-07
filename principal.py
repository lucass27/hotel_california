from funciones import *

opciones_menu()
opcion = ingresarOpcion()

reservas = []

def ejecutar_menu(opcion):
    if opcion == 1:
        cantidad_reservas = int(input("ingrese cuantas reservas quiere realizar: "))
        while cantidad_reservas > 60 or cantidad_reservas < 0:
            cantidad_reservas = int(input("El número maximo de reservas es 60 y no debe ser negativo. ingrese una cantidad válida: "))
        for i in range(cantidad_reservas):
            print("RESERVA NUMERO ",i+1)
            piso = int(input("ingrese el piso de habitación a reservar (entre 1 y 6): "))
            numero = int(input("ingrese el numero de habitacion correspondiente al piso: "))
            reservar_habitacion(piso,numero)
            cantidad_noches = int(input("ingrese cantidad de noches: "))
            asignar_noches(piso,numero,cantidad_noches)
            precioxnoche = ver_precio(piso,numero)
            preciototal = precioxnoche * cantidad_noches
            print("el precio por ",cantidad_noches," noches es: ",preciototal)
            categoria = ver_categoria(piso,numero)
            print("la categoria es: ",categoria)
            nombre = asignar_huesped(piso,numero)
            asignar_servicio(piso,numero)
            asignar_estadoReserva(piso,numero)
            info = [nombre,cantidad_noches]
            reservas.append(info)
        opciones_menu()
        opcion = ingresarOpcion()
        ejecutar_menu(opcion)

    if opcion == 2:
        piso = int(input("ingrese el piso de habitación a eliminar (entre 1 y 6): "))
        numero = int(input("ingrese el numero de habitacion correspondiente al piso: "))
        respuesta = int(input("esta seguro que quiere eliminar la habitacion ?. (1=SI | 2=NO)"))
        if respuesta == 1:
            estado = ver_estadoReserva_individual(piso,numero)
            if estado == 1:
                print("No se puede eliminar porque la reserva ya fue confirmada")
                opciones_menu()
                opcion = ingresarOpcion()
                ejecutar_menu(opcion)
            else:
                eliminar_habitacion(piso,numero)
                eliminar_huesped(piso,numero)
                eliminar_servicio(piso,numero)
                eliminar_estadoReserva(piso,numero)
                opciones_menu()
                opcion = ingresarOpcion()
                ejecutar_menu(opcion)
        else:
            opciones_menu()
            opcion = ingresarOpcion()  
            ejecutar_menu(opcion)      
    
    if opcion == 3:
        piso = int(input("ingrese el piso de habitación a modificar (entre 1 y 6): "))
        numero = int(input("ingrese el numero de habitacion correspondiente al piso: "))
        respuesta = int(input(" modificar huésped (1) \n modificar estado (2) \n modificar ambas (3) \n ingrese opción: "))
        if respuesta == 1:
            asignar_huesped(piso,numero)
            opciones_menu()
            opcion = ingresarOpcion()  
            ejecutar_menu(opcion) 
        elif respuesta == 2:
            asignar_estadoReserva(piso,numero)
            opciones_menu()
            opcion = ingresarOpcion()  
            ejecutar_menu(opcion) 
        else:
            asignar_huesped(piso,numero)
            asignar_estadoReserva(piso,numero)
            opciones_menu()
            opcion = ingresarOpcion()  
            ejecutar_menu(opcion)
    
    if opcion == 4:
        reservas_ordenadas = ordenar_reservas(reservas)
        print(reservas_ordenadas)

    if opcion == 5:
        ver_reservas()
        ver_huesped()
        ver_servicios()
        ver_estadoReserva()


ejecutar_menu(opcion)