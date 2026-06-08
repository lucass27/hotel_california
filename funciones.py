piso1_numero = [101,102,103,104,105,106,107,108,109,110]
piso1_categoria = ["estandar","estandar","estandar","estandar","estandar","estandar","estandar","estandar","suite","suite"]
piso1_reservada = [False,False,False,False,False,False,False,False,False,False]
piso1_servicio = [0,0,0,0,0,0,0,0,0,0] #0 es que no tiene ningun servicio.
piso1_huesped = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay ningun huesped asignado a la habitación.
piso1_estadoReserva = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay estado de reserva porque no fue reservada la habitación.
piso1_noches = [0,0,0,0,0,0,0,0,0,0]

piso2_numero = [201,202,203,204,205,206,207,208,209,210]
piso2_categoria = ["estandar","estandar","estandar","estandar","estandar","estandar","estandar","estandar","suite","suite"]
piso2_reservada = [False,False,False,False,False,False,False,False,False,False]
piso2_servicio = [0,0,0,0,0,0,0,0,0,0] #0 es que no tiene ningun servicio
piso2_huesped = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay ningun huesped asignado a la habitación
piso2_estadoReserva = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay estado de reserva porque no fue reservada la habitación.
piso2_noches = [0,0,0,0,0,0,0,0,0,0]

piso3_numero = [301,302,303,304,305,306,307,308,309,310]
piso3_categoria = ["estandar","estandar","estandar","estandar","estandar","estandar","estandar","estandar","suite","suite"]
piso3_reservada = [False,False,False,False,False,False,False,False,False,False]
piso3_servicio = [0,0,0,0,0,0,0,0,0,0] #0 es que no tiene ningun servicio
piso3_huesped = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay ningun huesped asignado a la habitación
piso3_estadoReserva = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay estado de reserva porque no fue reservada la habitación.
piso3_noches = [0,0,0,0,0,0,0,0,0,0]

piso4_numero = [401,402,403,404,405,406,407,408,409,410]
piso4_categoria = ["estandar","estandar","estandar","estandar","estandar","estandar","estandar","estandar","suite","suite"]
piso4_reservada = [False,False,False,False,False,False,False,False,False,False]
piso4_servicio = [0,0,0,0,0,0,0,0,0,0] #0 es que no tiene ningun servicio
piso4_huesped = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay ningun huesped asignado a la habitación
piso4_estadoReserva = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay estado de reserva porque no fue reservada la habitación.
piso4_noches = [0,0,0,0,0,0,0,0,0,0]

piso5_numero = [501,502,503,504,505,506,507,508,509,510]
piso5_categoria = ["estandar","estandar","estandar","estandar","estandar","estandar","estandar","estandar","suite","suite"]
piso5_reservada = [False,False,False,False,False,False,False,False,False,False]
piso5_servicio = [0,0,0,0,0,0,0,0,0,0] #0 es que no tiene ningun servicio
piso5_huesped = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay ningun huesped asignado a la habitación
piso5_estadoReserva = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay estado de reserva porque no fue reservada la habitación.
piso4_noches = [0,0,0,0,0,0,0,0,0,0]

piso6_numero = [601,602,603,604,605,606,607,608,609,610]
piso6_categoria = ["Premium","Premium","Premium","Premium","Premium","Premium","Premium","Premium","Premium","Premium",]
piso6_reservada = [False,False,False,False,False,False,False,False,False,False]
piso6_servicio = [0,0,0,0,0,0,0,0,0,0] #0 es que no tiene ningun servicio
piso6_huesped = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay ningun huesped asignado a la habitación
piso6_estadoReserva = [0,0,0,0,0,0,0,0,0,0] #0 es que no hay estado de reserva porque no fue reservada la habitación.
piso6_noches = [0,0,0,0,0,0,0,0,0,0]

def opciones_menu():
    """Función que muestra el menú con las opciones disponibles"""
    print("========================== \n LURABÉ FRASANÇ RESORT \n ========================= ")
    print("1. Registrar nueva reserva")      # muestra la opción 1
    print("2. Eliminar reserva")             # muestra la opción 2
    print("3. Modificar huesped o estado")   # muestra la opción 3
    print("4. Informe general de reservas")  # muestra la opción 4
    print("5. Salir")                        # muestra la opción 5
    print("==========================")
    print(" ")


def ingresarOpcion():
    """Función que pide una opción al usuario y la valida (que sea del 1 al 5)"""
    opcion = int(input("Ingrese una opción: "))  
    while opcion < 1 or opcion > 5:               
        print("Opción no válida. Por favor, ingrese una opción válida.")  
        opcion = int(input("Ingrese una opción: "))   
    return opcion   

def ver_hotel():
    """muestra las habitaciones en cuadricula"""
    print("HABITACIONES NUMERADAS \n ====================")
    print("piso 1", piso1_numero)
    print("piso 2", piso2_numero)
    print("piso 3", piso3_numero)
    print("piso 4", piso4_numero)
    print("piso 5", piso5_numero)
    print("piso 6", piso6_numero)

def ver_reservas():
    """muestra las reservas en cuadricula (confirmadas o no por true y false)"""
    print("RESERVAS CONFIRMADAS \n ====================")
    print("piso 1", piso1_reservada)
    print("piso 2", piso2_reservada)
    print("piso 3", piso3_reservada)
    print("piso 4", piso4_reservada)
    print("piso 5", piso5_reservada)
    print("piso 6", piso6_reservada)

def ver_servicios():
    """muestra los servicios asociados a las habitaciones en cuadricula"""
    print("ESTADOS DE SERVICIOS \n ====================")
    print("piso 1", piso1_servicio)
    print("piso 2", piso2_servicio)
    print("piso 3", piso3_servicio)
    print("piso 4", piso4_servicio)
    print("piso 5", piso5_servicio)
    print("piso 6", piso6_servicio)

def ver_huesped():
    """muestra los huespedes de cada habitacion por cuadricula"""
    print("HUESPED POR HABITACION \n ====================")
    print("piso 1", piso1_huesped)
    print("piso 2", piso2_huesped)
    print("piso 3", piso3_huesped)
    print("piso 4", piso4_huesped)
    print("piso 5", piso5_huesped)
    print("piso 6", piso6_huesped)

def ver_estadoReserva():
    """ver estados de reserva por cuadricula"""
    print("ESTADOS DE RESERVA \n ====================")
    print("piso 1", piso1_estadoReserva)
    print("piso 2", piso2_estadoReserva)
    print("piso 3", piso3_estadoReserva)
    print("piso 4", piso4_estadoReserva)
    print("piso 5", piso5_estadoReserva)
    print("piso 6", piso6_estadoReserva)

def verificar_reservada(piso,numero):
    """devuelve true si esta reservada y false si no lo está"""
    estado = False
    if piso == 1:
        if piso1_reservada[numero-101] == False:
            print("la habitación no está reservada")
        else:
            estado = True
            print("la habitación está reservada")
    elif piso == 2:
        if piso2_reservada[numero-201] == False:
            print("la habitación no está reservada")
        else:
            estado = True
            print("la habitación está reservada")
    elif piso == 3:
        if piso3_reservada[numero-301] == False:
            print("la habitación no está reservada")
        else:
            estado = True
            print("la habitación está reservada")
    elif piso == 4:
        if piso4_reservada[numero-401] == False:
            print("la habitación no está reservada")
        else:
            estado = True
            print("la habitación está reservada")
    elif piso == 5:
        if piso5_reservada[numero-501] == False:
            print("la habitación no está reservada")
        else:
            estado = True
            print("la habitación está reservada")
    else:
        if piso6_reservada[numero-601] == False:
            print("la habitación no está reservada")
        else:
            estado = True
            print("la habitación está reservada")
    return estado

def ver_categoria(piso,numero):
    """funcion que le pasas una habitacion y devuelve la categoria""" 
    categoria = " "
    if piso == 1:
        categoria = piso1_categoria[numero-101]
    elif piso == 2:
        categoria = piso2_categoria[numero-201]
    elif piso == 3:
        categoria = piso3_categoria[numero-301]
    elif piso == 4:
        categoria = piso4_categoria[numero-401]
    elif piso == 5:
        categoria = piso5_categoria[numero-501]
    else:
        categoria = piso6_categoria[numero-601]
    return categoria


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

def eliminar_servicio(piso,numero):
    """eliminar un servicio a una habitacion"""
    if piso == 1:
        piso1_servicio[numero-101] = 0
    if piso == 2:
        piso2_servicio[numero-201] = 0
    if piso == 3:
        piso3_servicio[numero-301] = 0
    if piso == 4:
        piso4_servicio[numero-401] = 0
    if piso == 5:
        piso5_servicio[numero-501] = 0
    if piso == 6:
        piso6_servicio[numero-601] = 0

def asignar_noches(piso,numero,noches):
    """eliminar un servicio a una habitacion"""
    if piso == 1:
        piso1_noches[numero-101] = noches
    if piso == 2:
        piso2_noches[numero-201] = noches
    if piso == 3:
        piso3_noches[numero-301] = noches
    if piso == 4:
        piso4_noches[numero-401] = noches
    if piso == 5:
        piso5_noches[numero-501] = noches
    if piso == 6:
        piso6_noches[numero-601] = noches

def asignar_huesped(piso,numero):
    """asignar huesped a habitacion"""
    nombre = str(input("ingrese el nombre del huesped: "))
    apellido = str(input("ingrese el apellido del huesped: "))
    nombreCompleto = nombre+" "+apellido
    if piso == 1:
        piso1_huesped[numero-101] = nombre+" "+apellido
    elif piso == 2:
        piso2_huesped[numero-201] = nombre+" "+apellido
    elif piso == 3:
        piso3_huesped[numero-301] = nombre+" "+apellido
    elif piso == 4:
        piso4_huesped[numero-401] = nombre+" "+apellido
    elif piso == 5:
        piso5_huesped[numero-501] = nombre+" "+apellido
    else:
        piso6_huesped[numero-601] = nombre+" "+apellido
    return nombreCompleto

def eliminar_huesped(piso,numero):
    """eliminar huesped de habitacion"""
    if piso == 1:
        piso1_huesped[numero-101] = 0
    elif piso == 2:
        piso2_huesped[numero-201] = 0
    elif piso == 3:
        piso3_huesped[numero-301] = 0
    elif piso == 4:
        piso4_huesped[numero-401] = 0
    elif piso == 5:
        piso5_huesped[numero-501] = 0
    else:
        piso6_huesped[numero-601] = 0

def asignar_estadoReserva(piso,numero):
    """asigna el estado de reserva a una reserva"""
    estado = int(input("Cual es el estado de la reserva: \n Confirmada (1) \n Provisoria (2) \n Cancelada (3) \n ingrese valor: "))
    if piso == 1:
        piso1_estadoReserva[numero-101] = estado
    if piso == 2:
        piso2_estadoReserva[numero-201] = estado
    if piso == 3:
        piso3_estadoReserva[numero-301] = estado
    if piso == 4:
        piso4_estadoReserva[numero-401] = estado
    if piso == 5:
        piso5_estadoReserva[numero-501] = estado
    if piso == 6:
        piso6_estadoReserva[numero-601] = estado

def eliminar_estadoReserva(piso,numero):
    """elimina el estado de una reserva dejandolo en 0"""
    if piso == 1:
        piso1_estadoReserva[numero-101] = 0
    if piso == 2:
        piso2_estadoReserva[numero-201] = 0
    if piso == 3:
        piso3_estadoReserva[numero-301] = 0
    if piso == 4:
        piso4_estadoReserva[numero-401] = 0
    if piso == 5:
        piso5_estadoReserva[numero-501] = 0
    if piso == 6:
        piso6_estadoReserva[numero-601] = 0


def ver_estadoReserva_individual(piso,numero):
    """funcion que le pasas una habitacion por piso y numero y te dice cual es el estado de reserva de ese identificador"""
    estado = 0
    if piso == 1:
        estado = piso1_estadoReserva[numero-101]
    if piso == 2:
        estado = piso2_estadoReserva[numero-201]
    if piso == 3:
        estado = piso3_estadoReserva[numero-301] 
    if piso == 4:
        estado = piso4_estadoReserva[numero-401] 
    if piso == 5:
        estado = piso5_estadoReserva[numero-501] 
    if piso == 6:
        estado = piso6_estadoReserva[numero-601]
    return estado

def reservar_habitacion(piso,numero):
    """se ingresa el piso y numero de habitacion a reservar"""
    """si ya esta reservada, no te la deja reservar, y te pide otra"""
    if piso == 1:
        if piso1_reservada[numero-101] == True:
            print("la habitacion ya esta resevada")
            print("ingrese otra habitacion: ")
            piso2 = int(input("ingrese piso: "))
            numero2 = int(input("ingrese habitacion: "))
            while piso_valido(piso,numero) != True:
                piso2 = int(input("ingrese piso valido: "))
                numero2 = int(input("ingrese número de habitación valido: "))
            reservar_habitacion(piso2,numero2)
        else:
            piso1_reservada[numero-101] = True
    elif piso == 2:
        if piso2_reservada[numero-201] == True:
            print("la habitacion ya esta resevada")
            print("ingrese otra habitacion: ")
            piso2 = int(input("ingrese piso: "))
            numero2 = int(input("ingrese habitacion: "))
            while piso_valido(piso,numero) != True:
                piso2 = int(input("ingrese piso valido: "))
                numero2 = int(input("ingrese número de habitación valido: "))
            reservar_habitacion(piso2,numero2)
        else:
            piso2_reservada[numero-201] = True
    elif piso == 3:
        if piso3_reservada[numero-301] == True:
            print("la habitacion ya esta resevada")
            print("ingrese otra habitacion: ")
            piso2 = int(input("ingrese piso: "))
            numero2 = int(input("ingrese habitacion: "))
            while piso_valido(piso,numero) != True:
                piso2 = int(input("ingrese piso valido: "))
                numero2 = int(input("ingrese número de habitación valido: "))
            reservar_habitacion(piso2,numero2)
        else:
            piso3_reservada[numero-301] = True
    elif piso == 4:
        if piso4_reservada[numero-401] == True:
            print("la habitacion ya esta resevada")
            print("ingrese otra habitacion: ")
            piso2 = int(input("ingrese piso: "))
            numero2 = int(input("ingrese habitacion: "))
            while piso_valido(piso,numero) != True:
                piso2 = int(input("ingrese piso valido: "))
                numero2 = int(input("ingrese número de habitación valido: "))
            reservar_habitacion(piso2,numero2)
        else:
            piso4_reservada[numero-401] = True
    elif piso == 5:
        if piso5_reservada[numero-501] == True:
            print("la habitacion ya esta resevada")
            print("ingrese otra habitacion: ")
            piso2 = int(input("ingrese piso: "))
            numero2 = int(input("ingrese habitacion: "))
            while piso_valido(piso,numero) != True:
                piso2 = int(input("ingrese piso valido: "))
                numero2 = int(input("ingrese número de habitación valido: "))
            reservar_habitacion(piso2,numero2)
        else:
            piso5_reservada[numero-501] = True
    else:
        if piso6_reservada[numero-601] == True:
            print("la habitacion ya esta resevada")
            print("ingrese otra habitacion: ")
            piso2 = int(input("ingrese piso: "))
            numero2 = int(input("ingrese habitacion: "))
            while piso_valido(piso,numero) != True:
                piso2 = int(input("ingrese piso valido: "))
                numero2 = int(input("ingrese número de habitación valido: "))
            reservar_habitacion(piso2,numero2)
        else:
            piso6_reservada[numero-601] = True

def eliminar_habitacion(piso,numero):
    """se ingresa el piso y numero de habitacion a eliminar"""
    """si no esté reservada, no te la deja eliminar, y te pide otra"""
    if piso == 1:
        if piso1_reservada[numero-101] == False:
            print("la habitacion no está resevada")
            print("ingrese otra habitacion que si la esté: ")
            piso2 = int(input("ingrese piso: "))
            numero2 = int(input("ingrese habitacion: "))
            while piso_valido(piso,numero) != True:
                piso2 = int(input("ingrese piso valido: "))
                numero2 = int(input("ingrese número de habitación valido: "))
            reservar_habitacion(piso2,numero2)
        else:
            piso1_reservada[numero-101] = False
    elif piso == 2:
        if piso2_reservada[numero-201] == False:
            print("la habitacion no está resevada")
            print("ingrese otra habitacion que si la esté: ")
            piso2 = int(input("ingrese piso: "))
            numero2 = int(input("ingrese habitacion: "))
            while piso_valido(piso,numero) != True:
                piso2 = int(input("ingrese piso valido: "))
                numero2 = int(input("ingrese número de habitación valido: "))
            reservar_habitacion(piso2,numero2)
        else:
            piso2_reservada[numero-201] = False
    elif piso == 3:
        if piso3_reservada[numero-301] == False:
            print("la habitacion no está resevada")
            print("ingrese otra habitacion que si la esté: ")
            piso2 = int(input("ingrese piso: "))
            numero2 = int(input("ingrese habitacion: "))
            while piso_valido(piso,numero) != True:
                piso2 = int(input("ingrese piso valido: "))
                numero2 = int(input("ingrese número de habitación valido: "))
            reservar_habitacion(piso2,numero2)
        else:
            piso3_reservada[numero-301] = False
    elif piso == 4:
        if piso4_reservada[numero-401] == False:
            print("la habitacion no está resevada")
            print("ingrese otra habitacion que si la esté: ")
            piso2 = int(input("ingrese piso: "))
            numero2 = int(input("ingrese habitacion: "))
            while piso_valido(piso,numero) != True:
                piso2 = int(input("ingrese piso valido: "))
                numero2 = int(input("ingrese número de habitación valido: "))
            reservar_habitacion(piso2,numero2)
        else:
            piso4_reservada[numero-401] = False
    elif piso == 5:
        if piso5_reservada[numero-501] == False:
            print("la habitacion no está resevada")
            print("ingrese otra habitacion que si la esté: ")
            piso2 = int(input("ingrese piso: "))
            numero2 = int(input("ingrese habitacion: "))
            while piso_valido(piso,numero) != True:
                piso2 = int(input("ingrese piso valido: "))
                numero2 = int(input("ingrese número de habitación valido: "))
            reservar_habitacion(piso2,numero2)
        else:
            piso5_reservada[numero-501] = False
    else:
        if piso6_reservada[numero-601] == False:
            print("la habitacion no está resevada")
            print("ingrese otra habitacion que si la esté: ")
            piso2 = int(input("ingrese piso: "))
            numero2 = int(input("ingrese habitacion: "))
            while piso_valido(piso,numero) != True:
                piso2 = int(input("ingrese piso valido: "))
                numero2 = int(input("ingrese número de habitación valido: "))
            reservar_habitacion(piso2,numero2)
        else:
            piso6_reservada[numero-601] = False

def piso_valido(piso,numero):
    """funcion que chequea que el piso y numero sea valido"""
    respuesta = False
    if piso >= 1 and piso <= 6:
        if piso == 1:
            if numero >= 101 and numero <= 110:
                respuesta = True
            else:
                respuesta = False
        if piso == 2:
            if numero >= 201 and numero <= 210:
                respuesta = True
            else:
                respuesta = False
        if piso == 3:
            if numero >= 301 and numero <= 310:
                respuesta = True
            else:
                respuesta = False
        if piso == 4:
            if numero >= 401 and numero <= 410:
                respuesta = True
            else:
                respuesta = False
        if piso == 5:
            if numero >= 501 and numero <= 510:
                respuesta = True
            else:
                respuesta = False
        if piso == 6:
            if numero >= 601 and numero <= 610:
                respuesta = True
            else:
                respuesta = False
    else:
        respuesta = False
    return respuesta

def ver_huesped_individual(piso, numero):
    """devuelve el nombre del huesped de una habitacion especifica"""
    if piso == 1:
        return piso1_huesped[numero - 101]
    elif piso == 2:
        return piso2_huesped[numero - 201]
    elif piso == 3:
        return piso3_huesped[numero - 301]
    elif piso == 4:
        return piso4_huesped[numero - 401]
    elif piso == 5:
        return piso5_huesped[numero - 501]
    else:
        return piso6_huesped[numero - 601]
    

def ordenar_reservas(reservas):
    """Ordena una lista de reservas de mayor a menor según la cantidad de noches. 
    En caso de empate en las noches, ordena alfabéticamente por el nombre del huésped."""
    n = len(reservas)
    for i in range(n):
        for j in range(0, n - i - 1):
            a = reservas[j]
            b = reservas[j + 1]
            
            # Comparar: si a tiene menos noches, o mismas noches pero nombre mayor alfabéticamente
            if a[1] < b[1] or (a[1] == b[1] and a[0] > b[0]):
                reservas[j], reservas[j + 1] = reservas[j + 1], reservas[j]
    
    return reservas