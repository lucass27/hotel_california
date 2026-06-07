from funciones import *

opciones_menu()
opcion = ingresarOpcion()

if opcion == 1:
    cantidad_reservas = int(input("ingrese cuantas reservas quiere realizar: "))
    while cantidad_reservas > 60 or cantidad_reservas < 0:
        cantidad_reservas = int(input("El número maximo de reservas es 60 y no debe ser negativo. ingrese una cantidad válida: "))
    for i in range(cantidad_reservas):
        print("RESERVA NUMERO ",i)
        piso = int(input("ingrese el piso de habitación a reservar (entre 1 y 6): "))
        numero = int(input("ingrese el numero de habitacion correspondiente al piso: "))
        reservar_habitacion(piso,numero)
        cantidad_noches = int(input("ingrese cantidad de noches: "))
        precioxnoche = ver_precio(piso,numero)
        preciototal = precioxnoche * cantidad_noches
        print("el precio por ",cantidad_noches," noches es: ",preciototal)
        categoria = ver_categoria(piso,numero)
        print("la categoria es: ",categoria)
        asignar_huesped(piso,numero)
        asignar_servicio(piso,numero)
        asignar_estadoReserva(piso,numero)
if opcion == 2:
    

ver_reservas()
ver_huesped()
ver_servicios()
ver_estadoReserva()
