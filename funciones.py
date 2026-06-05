piso1_numero = [101,102,103,104,105,106,107,108,109,110]
piso1_categoria = ["estandar","estandar","estandar","estandar","estandar","estandar","estandar","estandar","suite","suite"]
piso1_reservada = [False,False,False,False,False,False,False,False,False,False]
piso1_servicio = [0,0,0,0,0,0,0,0,0,0] #0 es que no tiene ningun servicio
piso1_huesped = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay ningun huesped asignado a la habitación

piso2_numero = [201,202,203,204,205,206,207,208,209,210]
piso2_categoria = ["estandar","estandar","estandar","estandar","estandar","estandar","estandar","estandar","suite","suite"]
piso2_reservada = [False,False,False,False,False,False,False,False,False,False]
piso2_servicio = [0,0,0,0,0,0,0,0,0,0] #0 es que no tiene ningun servicio
piso2_huesped = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay ningun huesped asignado a la habitación

piso3_numero = [301,302,303,304,305,306,307,308,309,310]
piso3_categoria = ["estandar","estandar","estandar","estandar","estandar","estandar","estandar","estandar","suite","suite"]
piso3_reservada = [False,False,False,False,False,False,False,False,False,False]
piso3_servicio = [0,0,0,0,0,0,0,0,0,0] #0 es que no tiene ningun servicio
piso3_huesped = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay ningun huesped asignado a la habitación

piso4_numero = [401,402,403,404,405,406,407,408,409,410]
piso4_categoria = ["estandar","estandar","estandar","estandar","estandar","estandar","estandar","estandar","suite","suite"]
piso4_reservada = [False,False,False,False,False,False,False,False,False,False]
piso4_servicio = [0,0,0,0,0,0,0,0,0,0] #0 es que no tiene ningun servicio
piso4_huesped = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay ningun huesped asignado a la habitación

piso5_numero = [501,502,503,504,505,506,507,508,509,510]
piso5_categoria = ["estandar","estandar","estandar","estandar","estandar","estandar","estandar","estandar","suite","suite"]
piso5_reservada = [False,False,False,False,False,False,False,False,False,False]
piso5_servicio = [0,0,0,0,0,0,0,0,0,0] #0 es que no tiene ningun servicio
piso5_huesped = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay ningun huesped asignado a la habitación

piso6_numero = [601,602,603,604,605,606,607,608,609,610]
piso6_categoria = ["Premium","Premium","Premium","Premium","Premium","Premium","Premium","Premium","Premium","Premium",]
piso6_reservada = [False,False,False,False,False,False,False,False,False,False]
piso6_servicio = [0,0,0,0,0,0,0,0,0,0] #0 es que no tiene ningun servicio
piso6_huesped = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay ningun huesped asignado a la habitación

# Función que muestra el menú con las opciones disponibles
def opciones_menu():
    print("1. Registrar nueva reserva")      # muestra la opción 1
    print("2. Eliminar reserva")             # muestra la opción 2
    print("3. Modificar huesped o estado")   # muestra la opción 3
    print("4. Informe general de reservas")  # muestra la opción 4
    print("5. Salir")                        # muestra la opción 5

# Función que pide una opción al usuario y la valida (que sea del 1 al 5)
def ingresarOpcion():
    opcion = int(input("Ingrese una opción: "))   # pide un número y lo convierte a entero
    while opcion < 1 or opcion > 5:               # mientras el número esté fuera del rango 1-5...
        print("Opción no válida. Por favor, ingrese una opción válida.")  # avisa que está mal
        opcion = int(input("Ingrese una opción: "))   # vuelve a pedir el número
    return opcion   # devuelve la opción válida

def ver_hotel():
    print(piso1_numero)
    print(piso2_numero)
    print(piso3_numero)
    print(piso4_numero)
    print(piso5_numero)
    print(piso6_numero)

def ver_reservas():
    print(piso1_reservada)
    print(piso2_reservada)
    print(piso3_reservada)
    print(piso4_reservada)
    print(piso5_reservada)
    print(piso6_reservada)

def ver_servicios():
    print(piso1_servicio)
    print(piso2_servicio)
    print(piso3_servicio)
    print(piso4_servicio)
    print(piso5_servicio)
    print(piso6_servicio)

def ver_huesped():
    print(piso1_huesped)
    print(piso2_huesped)
    print(piso3_huesped)
    print(piso4_huesped)
    print(piso5_huesped)
    print(piso6_huesped)

def ver_precio(piso,numero):
    """funcion que le pasas una habitacion y devuelve el precio"""
    if piso == 1:
        if piso1_categoria[numero-101] == "estandar":
            precio = 150
        else:
            precio = 300
    if piso == 2:
        if piso2_categoria[numero-201] == "estandar":
            precio = 150
        else:
            precio = 300
    if piso == 3:
        if piso3_categoria[numero-301] == "estandar":
            precio = 150
        else:
            precio = 300
    if piso == 4:
        if piso4_categoria[numero-401] == "estandar":
            precio = 150
        else:
            precio = 300
    if piso == 5:
        if piso5_categoria[numero-501] == "estandar":
            precio = 150
        else:
            precio = 300
    if piso == 6:
        precio = 500
    return precio

def asignar_servicio(piso,numero):
    """asignar un servicio a una habitacion"""
    servicio = int(input("Que servicio quiere agregar?: \n Ninguno (0) \n Desayuno(1) \n Spa(2) \n Estacionamiento (3) \n Acceso Premium (4) \n ingrese opción: "))
    if piso == 1:
        if servicio == 1:
            piso1_servicio[numero-101] = 1
        elif servicio == 2:
            piso1_servicio[numero-101] = 2
        elif servicio == 3:
            piso1_servicio[numero-101] = 3
        else:
            piso1_servicio[numero-101] = 4
    if piso == 2:
        if servicio == 1:
            piso2_servicio[numero-201] = 1
        elif servicio == 2:
            piso2_servicio[numero-201] = 2
        elif servicio == 3:
            piso2_servicio[numero-201] = 3
        else:
            piso2_servicio[numero-201] = 4
    if piso == 3:
        if servicio == 1:
            piso3_servicio[numero-301] = 1
        elif servicio == 2:
            piso3_servicio[numero-301] = 2
        elif servicio == 3:
            piso3_servicio[numero-301] = 3
        else:
            piso3_servicio[numero-301] = 4
    if piso == 4:
        if servicio == 1:
            piso4_servicio[numero-401] = 1
        elif servicio == 2:
            piso4_servicio[numero-401] = 2
        elif servicio == 3:
            piso4_servicio[numero-401] = 3
        else:
            piso4_servicio[numero-401] = 4
    if piso == 5:
        if servicio == 1:
            piso5_servicio[numero-501] = 1
        elif servicio == 2:
            piso5_servicio[numero-501] = 2
        elif servicio == 3:
            piso5_servicio[numero-501] = 3
        else:
            piso5_servicio[numero-501] = 4
    if piso == 6:
        if servicio == 1:
            piso6_servicio[numero-601] = 1
        elif servicio == 2:
            piso6_servicio[numero-601] = 2
        elif servicio == 3:
            piso6_servicio[numero-601] = 3
        else:
            piso6_servicio[numero-601] = 4
    return servicio

def asignar_huesped(piso,numero):
    if piso == 1:
        nombre = str(input("ingrese el nombre del huesped: "))
        apellido = str(input("ingrese el apellido del huesped: "))
        piso1_huesped[numero-101] = nombre+" "+apellido
    if piso == 2:
        nombre = str(input("ingrese el nombre del huesped: "))
        apellido = str(input("ingrese el apellido del huesped: "))
        piso2_huesped[numero-201] = nombre+" "+apellido
    if piso == 3:
        nombre = str(input("ingrese el nombre del huesped: "))
        apellido = str(input("ingrese el apellido del huesped: "))
        piso3_huesped[numero-301] = nombre+" "+apellido
    if piso == 4:
        nombre = str(input("ingrese el nombre del huesped: "))
        apellido = str(input("ingrese el apellido del huesped: "))
        piso4_huesped[numero-401] = nombre+" "+apellido
    if piso == 5:
        nombre = str(input("ingrese el nombre del huesped: "))
        apellido = str(input("ingrese el apellido del huesped: "))
        piso5_huesped[numero-501] = nombre+" "+apellido
    if piso == 6:
        nombre = str(input("ingrese el nombre del huesped: "))
        apellido = str(input("ingrese el apellido del huesped: "))
        piso6_huesped[numero-601] = nombre+" "+apellido




def reservar_habitacion(piso,numero):
    """se ingresa el piso y numero de habitacion a reservar"""
    """si ya esta reservada, no te la deja reservar"""
    if piso == 1:
        if piso1_reservada[numero-101] == True:
            print("la habitacion ya esta resevada")
        else:
            piso1_reservada[numero-101] = True
    elif piso == 2:
        if piso1_reservada[numero-201] == True:
            print("la habitacion ya esta resevada")
        else:
            piso2_reservada[numero-201] = True
    elif piso == 3:
        if piso1_reservada[numero-301] == True:
            print("la habitacion ya esta resevada")
        else:
            piso3_reservada[numero-301] = True
    elif piso == 4:
        if piso1_reservada[numero-401] == True:
            print("la habitacion ya esta resevada")
        else:
            piso4_reservada[numero-401] = True
    elif piso == 5:
        if piso1_reservada[numero-501] == True:
            print("la habitacion ya esta resevada")
        else:
            piso5_reservada[numero-501] = True
    else:
        if piso1_reservada[numero-601] == True:
            print("la habitacion ya esta resevada")
        else:
            piso6_reservada[numero-601] = True

def opcion1():
        print("reservas actuales: ")
        ver_reservas()
        print("RESERVAR: ")
        piso = int(input("ingrese el piso: "))
        numero = int(input("ingrese el numero de habitacion: "))
        reservar_habitacion(piso,numero)
        print("RESERVA CONFIRMADA. ASI QUEDO: ")
        ver_reservas()
        print("quiere realizar otra reserva? (SI/NO)")
        rta = str(input())
        if rta == "SI":
            opcion1()