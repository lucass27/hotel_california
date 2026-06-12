

def crear_hotel(pisos,habitacionesxpiso):
    """la función crear hotel tomo como parámetros la cantidad de pisos y habitaciones 
    por cada piso que se quiere crear. siempre el ultimo piso serán todas habitaciones de categoría premium.
    cada habitación contiene los siguientes datos en orden:
        1) numero de habitacion
        2) categoria de la habitacion (estandar, suite o premium)
        3) reservada o no (True/False)
        4) servicio (0:ninguno | 1:desayuno | 2:spa | estacionamiento:3 | acceso premium: 4)
        5) huesped (0:no hay ningun huesped)
        6) estado reserva (0:aun no fue reservada, | 1:confirmada | 2:provisoria | 3:cancelada)
        7) noches reservadas """
    hotel = []
    for piso in range(1, pisos + 1):
        for hab in range(1, habitacionesxpiso + 1):
            numero = piso * 100 + hab
            if piso == pisos:
                categoria = "premium"
            elif hab <= 8:
                categoria = "estandar"
            else:
                categoria = "suite"
            hotel.append([numero, categoria, False, 0, 0, 0, 0])
    return hotel

hotel = crear_hotel(6,10)

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
    opcion = input("Ingrese una opción: ")
    while opcion not in ["1","2","3","4","5"]:
        print("Opción no válida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese una opción: ")
    return int(opcion) 
    
def obtener_posicion(hotel, id_habitacion):
    """devuelve la posicion que le corresponde a un habitación en el hotel. 
    Por ejemplo la habitación 101 ocupa la posición 0 en el hotel"""
    for i in range(len(hotel)):
        if hotel[i][0] == id_habitacion:
            return i

def id_valido(hotel, id_habitacion):
    """devuelve True si es un id valido y False si no lo es."""
    for hab in hotel:
        if str(hab[0]) == id_habitacion:
            return True
    return False

def reservar_habitacion(id_habitacion):
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print("====ID inválido, ingrese uno correcto====")
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    habitacion = hotel[obtener_posicion(hotel, id_habitacion)]
    if habitacion[2] == True:
        print("La habitación ya está reservada, ingrese otra")
        id_habitacion = input("Ingrese el ID de la habitación: ")
        return reservar_habitacion(id_habitacion)
    hotel[obtener_posicion(hotel, id_habitacion)][2] = True
        
def asignar_huesped(id_habitacion):
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print("====ID inválido, ingrese uno correcto====")
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    habitacion = hotel[obtener_posicion(hotel, id_habitacion)]
    if habitacion[4] != 0:
        print("La habitación ya tiene un huésped asignado")
        id_habitacion = input("Ingrese el ID de la habitación: ")
        return asignar_huesped(id_habitacion)
    nombre = input("Ingrese el nombre del huésped: ")
    apellido = input("Ingrese el apellido del huésped: ")
    hotel[obtener_posicion(hotel, id_habitacion)][4] = nombre + " " + apellido

def asignar_servicio(id_habitacion):
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print("====ID inválido, ingrese uno correcto====")
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    print("Servicios disponibles:")
    print("0: Ninguno")
    print("1: Desayuno")
    print("2: Spa")
    print("3: Estacionamiento")
    print("4: Acceso premium")
    servicio = input("Ingrese el servicio a asignar: ")
    while servicio not in ["0","1","2","3","4"]:
        print("Servicio inválido, ingrese uno correcto")
        servicio = input("Ingrese el servicio a asignar: ")
    hotel[obtener_posicion(hotel, id_habitacion)][3] = int(servicio)

def asignar_estado_reserva(id_habitacion):
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print("ID inválido, ingrese uno correcto")
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    print("Estados disponibles:")
    print("0: Aún no fue reservada")
    print("1: Confirmada")
    print("2: Provisoria")
    print("3: Cancelada")
    estado = input("Ingrese el estado a asignar: ")
    while estado not in ["0","1","2","3"]:
        print("Estado inválido, ingrese uno correcto")
        estado = input("Ingrese el estado a asignar: ")
    hotel[obtener_posicion(hotel, id_habitacion)][5] = int(estado)

def ver_precio(id_habitacion):
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print("ID inválido, ingrese uno correcto")
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    habitacion = hotel[obtener_posicion(hotel, id_habitacion)]
    noches = habitacion[6]
    categoria = habitacion[1]
    if categoria == "estandar":
        precio = 150 * noches
    elif categoria == "suite":
        precio = 300 * noches
    else:
        precio = 500 * noches
    return precio

def es_numero_positivo(valor):
    digitos = "0123456789"
    if len(valor) == 0:
        return False
    for c in valor:
        encontrado = False
        for d in digitos:
            if c == d:
                encontrado = True
        if not encontrado:
            return False
    if int(valor) <= 0:
        return False
    return True

def asignar_noches(id_habitacion):
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print("ID inválido, ingrese uno correcto")
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    noches = input("Ingrese la cantidad de noches: ")
    while not es_numero_positivo(noches):
        print("Cantidad de noches inválida, ingrese una correcta")
        noches = input("Ingrese la cantidad de noches: ")
    hotel[obtener_posicion(hotel, id_habitacion)][6] = int(noches)

def eliminar_reserva(id_habitacion):
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print("ID inválido, ingrese uno correcto")
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    habitacion = hotel[obtener_posicion(hotel, id_habitacion)]
    if habitacion[5] == 2 or habitacion[5] == 3:
        hotel[obtener_posicion(hotel, id_habitacion)] = [id_habitacion, habitacion[1], False, 0, 0, 0, 0]
    else:
        print("No se puede eliminar la reserva, el estado debe ser provisoria o cancelada")
        print("1: Ingresar otra habitación")
        print("2: Salir")
        opcion = input("Ingrese una opción: ")
        while opcion not in ["1","2"]:
            print("Opción inválida")
            opcion = input("Ingrese una opción: ")
        if opcion == "1":
            id_habitacion = input("Ingrese el ID de la habitación: ")
            return eliminar_reserva(id_habitacion)

def modificar_reserva(id_habitacion):
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print("ID inválido, ingrese uno correcto")
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    habitacion = hotel[obtener_posicion(hotel, id_habitacion)]
    if habitacion[2] == False:
        print("La habitación no tiene una reserva activa")
        return
    print("¿Qué desea modificar?")
    print("1: Huésped")
    print("2: Estado de reserva")
    print("3: Ambos")
    opcion = input("Ingrese una opción: ")
    while opcion not in ["1","2","3"]:
        print("Opción inválida")
        opcion = input("Ingrese una opción: ")
    if opcion == "1" or opcion == "3":
        nombre = input("Ingrese el nuevo nombre del huésped: ")
        apellido = input("Ingrese el nuevo apellido del huésped: ")
        hotel[obtener_posicion(hotel, id_habitacion)][4] = nombre + " " + apellido
    if opcion == "2" or opcion == "3":
        print("Estados disponibles:")
        print("0: Aún no fue reservada")
        print("1: Confirmada")
        print("2: Provisoria")
        print("3: Cancelada")
        estado = input("Ingrese el nuevo estado: ")
        while estado not in ["0","1","2","3"]:
            print("Estado inválido, ingrese uno correcto")
            estado = input("Ingrese el nuevo estado: ")
        hotel[obtener_posicion(hotel, id_habitacion)][5] = int(estado)
    print(f"Habitación {id_habitacion} modificada con éxito")

def informe_general():
    servicios = ["Ninguno", "Desayuno", "Spa", "Estacionamiento", "Acceso premium"]
    estados = ["Aún no fue reservada", "Confirmada", "Provisoria", "Cancelada"]
    
    reservadas = []
    for hab in hotel:
        if hab[2] == True:
            reservadas.append(hab)
    
    for i in range(len(reservadas)):
        for j in range(i + 1, len(reservadas)):
            if reservadas[i][6] < reservadas[j][6]:
                reservadas[i], reservadas[j] = reservadas[j], reservadas[i]
            elif reservadas[i][6] == reservadas[j][6] and reservadas[i][4] > reservadas[j][4]:
                reservadas[i], reservadas[j] = reservadas[j], reservadas[i]
    
    print("==================== INFORME GENERAL ====================")
    for hab in reservadas:
        print("Habitación: " + str(hab[0]) + " | Categoría: " + hab[1] + " | Huésped: " + str(hab[4]) + " | Noches: " + str(hab[6]) + " | Servicio: " + servicios[hab[3]] + " | Estado: " + estados[hab[5]])
    print("=========================================================")