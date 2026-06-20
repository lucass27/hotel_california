ROJO = "\033[91m"
VERDE = "\033[92m"
RESET = "\033[0m"

def crear_hotel(pisos,habitacionesxpiso):
    """la función crear hotel tomo como parámetros la cantidad de pisos y habitaciones 
    por cada piso que se quiere crear. siempre el ultimo piso serán todas habitaciones de categoría premium.
    cada habitación contiene los siguientes datos en orden:
        1) numero de habitacion
        2) categoria de la habitacion (estandar, suite o premium)
        3) estado de la habitacion: (0:bloqueada por mantenimiento | 1: disponible | 2:reservada)
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
            hotel.append([numero, categoria, 1, 0, 0, 0, 0])
    return hotel

hotel = crear_hotel(6,10)


def opciones_menu():
    """muestra las opciones del menu"""
    print(VERDE + "========================== \n LURABÉ FRASANÇ RESORT \n ========================= " + RESET)
    print("1. Registrar nueva reserva")
    print("2. Eliminar reserva")
    print("3. Modificar huésped o estado")
    print("4. Confirmar reserva provisoria")
    print("5. Informes")
    print("6. Gestión de habitaciones")
    print("7. Salir")
    print(VERDE + "==========================" + RESET)
    print(" ")

def ingresarOpcion():
    """pide al usuario una opción y valida que sea correcta"""
    opcion = input("Ingrese una opción: ")
    while opcion not in ["1","2","3","4","5","6","7"]:
        print(ROJO + "Opción no válida. Por favor, ingrese una opción válida." + RESET)
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
    """Función que recibe como parámetro un id de habitación y valida que sea correcto. 
    Luego cambia el estado de la reserva a True solo si esa habitación no tiene ninguna reserva activa. 
    En caso de tener una reserva activa pide otra habitación y se vuelve a llamar a la función."""
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print(ROJO + "====ID inválido, ingrese uno correcto====" + RESET)
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    habitacion = hotel[obtener_posicion(hotel, id_habitacion)]
    if habitacion[2] == 2:
        print(ROJO + "La habitación ya está reservada, ingrese otra" + RESET)
        id_habitacion = input("Ingrese el ID de la habitación: ")
        return reservar_habitacion(id_habitacion)
    elif habitacion[2] == 0:
        print(ROJO + "La habitación está Bloqueada por mantenimiento, ingrese otra" + RESET)
        id_habitacion = input("Ingrese el ID de la habitación: ")
        return reservar_habitacion(id_habitacion)
    else:
        hotel[obtener_posicion(hotel, id_habitacion)][2] = 2
    return id_habitacion

def asignar_huesped(id_habitacion):
    """Función que recibe como parámetro un id de habitación y valida que sea correcto. Luego pide al usuario un nombre y apellido y se lo asigna a esa habitación. 
    En el caso de que esa habitación ya tenga un huesped asignado, pide otro."""
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print(ROJO + "====ID inválido, ingrese uno correcto====" + RESET)
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    habitacion = hotel[obtener_posicion(hotel, id_habitacion)]
    if habitacion[4] != 0:
        print(ROJO + "La habitación ya tiene un huésped asignado" + RESET)
        id_habitacion = input("Ingrese el ID de la habitación: ")
        return asignar_huesped(id_habitacion)
    nombre = input("Ingrese el nombre del huésped: ")
    apellido = input("Ingrese el apellido del huésped: ")
    hotel[obtener_posicion(hotel, id_habitacion)][4] = nombre + " " + apellido
    return id_habitacion

def asignar_servicio(id_habitacion):
    """Función que recibe como parámetro un id de habitación y valida que sea correcto. 
    Luego le pide al usuario que le asigne un servicio adicional a la habitación el cual 
    también valida que sea correcto."""
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print(ROJO + "====ID inválido, ingrese uno correcto====" + RESET)
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
        print(ROJO + "Servicio inválido, ingrese uno correcto" + RESET)
        servicio = input("Ingrese el servicio a asignar: ")
    hotel[obtener_posicion(hotel, id_habitacion)][3] = int(servicio)

def asignar_estado_reserva(id_habitacion):
    """Función que recibe como parámetro un id de habitación y valida que sea correcto. 
    Luego le pide al usuario que le asigne un Estado de reserva a la habitación el cual 
    también valida que sea correcto."""
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print(ROJO + "====ID inválido, ingrese uno correcto====" + RESET)
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    print("Estados disponibles:")
    print("0: Aún no fue reservada")
    print("1: Confirmada")
    print("2: Provisoria")
    print("3: Cancelada")
    estado = input("Ingrese el estado a asignar: ")
    while estado not in ["0","1","2","3"]:
        print(ROJO + "Estado inválido, ingrese uno correcto" + RESET)
        estado = input("Ingrese el estado a asignar: ")
    hotel[obtener_posicion(hotel, id_habitacion)][5] = int(estado)

def asignar_estado_provisorio(id_habitacion):
    """asigna el estado provisorio a una habitacion"""
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print(ROJO + "====ID inválido, ingrese uno correcto====" + RESET)
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    hotel[obtener_posicion(hotel, id_habitacion)][5] = 2

def ver_precio(id_habitacion):
    """Función que recibe como parámetro un id de habitación y valida que sea correcto. 
    Retorna el precio de la reserva calculandoló con la categoría de la habitación y la cantidad de noches."""
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print(ROJO +"====ID inválido, ingrese uno correcto====" + RESET)
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
    """Recibe como parámetro un valor que puede ser de cualquier tipo (str, int, float) 
    y valida que un número sea positivo mediante el algoritmo de busqueda secuencial, 
    retornando True si lo es y False si no lo cumple"""
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
    """Función que recibe como parámetro un id de habitación y valida que sea correcto. 
    Luego le pide al usuario que ingrese un número de noches para asignarle a esa habitación"""
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print(ROJO + "====ID inválido, ingrese uno correcto====" + RESET)
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    noches = input("Ingrese la cantidad de noches: ")
    while not es_numero_positivo(noches):
        print(ROJO + "Cantidad de noches inválida, ingrese una correcta" + RESET)
        noches = input("Ingrese la cantidad de noches: ")
    hotel[obtener_posicion(hotel, id_habitacion)][6] = int(noches)

def eliminar_reserva(id_habitacion):
    """Función que recibe como parámetro un id de habitación y valida que sea correcto. 
    Luego elimina esa reserva solo si el estado de la reserva es provisoria o cancelada. 
    Elimina el huesped, la cantidad de noches y el estado de reserva y servicio adicional"""
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print(ROJO + "====ID inválido, ingrese uno correcto====" + RESET)
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    habitacion = hotel[obtener_posicion(hotel, id_habitacion)]
    if habitacion[5] == 2 or habitacion[5] == 3:
        decision = input("Esta seguro que desea eliminar la reserva? S / N : ")
        while decision not in ["S","s","N","n"]:
            print(ROJO + "Opción inválida" + RESET)
            decision = input("Ingrese una opción S / N: ")
        if decision == "S" or decision == "s":
            hotel[obtener_posicion(hotel, id_habitacion)] = [id_habitacion, habitacion[1], 1, 0, 0, 0, 0]
        else:
            return
    else:
        print(ROJO + "No se puede eliminar la reserva, el estado debe ser provisoria o cancelada" + RESET)
        print("1: Ingresar otra habitación")
        print("2: Salir")
        opcion = input("Ingrese una opción: ")
        while opcion not in ["1","2"]:
            print(ROJO + "Opción inválida" + RESET)
            opcion = input("Ingrese una opción: ")
        if opcion == "1":
            id_habitacion = input("Ingrese el ID de la habitación: ")
            return eliminar_reserva(id_habitacion)

def modificar_reserva(id_habitacion):
    """Función que recibe como parámetro un id de habitación y valida que sea correcto. 
    Le pregunta al usuario si quiere modificar el huesped, el estado de reserva o ambas, y realiza el cambio."""
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print(ROJO + "==ID inválido, ingrese uno correcto==" + RESET)
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    habitacion = hotel[obtener_posicion(hotel, id_habitacion)]
    if habitacion[2] != 2:
        print(ROJO + "La habitación no tiene una reserva activa" + RESET)
        return
    print("¿Qué desea modificar?")
    print("1: Huésped")
    print("2: Estado de reserva")
    print("3: Ambos")
    opcion = input("Ingrese una opción: ")
    while opcion not in ["1","2","3"]:
        print(ROJO + "Opción inválida" + RESET)
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
            print(ROJO + "Estado inválido, ingrese uno correcto" + RESET)
            estado = input("Ingrese el nuevo estado: ")
        hotel[obtener_posicion(hotel, id_habitacion)][5] = int(estado)

def confirmar_reserva(id_habitacion):
    """recibe como parámetro un id de habitacion y valida que sea correcto. Luego cambia el estado de la reserva de provisoria a confirmada"""
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print(ROJO + "====ID inválido, ingrese uno correcto====" + RESET)
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    habitacion = hotel[obtener_posicion(hotel, id_habitacion)]
    if habitacion[5] != 2:
        print(ROJO + "La reserva no está en estado provisorio, no se puede confirmar" + RESET)
        return
    hotel[obtener_posicion(hotel, id_habitacion)][5] = 1

def modificar_categoria(id_habitacion):
    """recibe como parámetro un id de habitacion y valida que sea correcto. luego modifica la categoria de una habitacion a elección. 
    Si ya esta reservada no se puede cambiar porque cambiaria el precio tambien por las noches que eligió"""
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print(ROJO + "====ID inválido, ingrese uno correcto====" + RESET)
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    habitacion = hotel[obtener_posicion(hotel, id_habitacion)]
    if habitacion[2] == 2:
        print(ROJO + "No se puede modificar la categoría de una habitación reservada" + RESET)
        return
    print("Categorías disponibles:")
    print("1: Estandar")
    print("2: Suite")
    print("3: Premium")
    categoria = input("Ingrese la nueva categoría: ")
    while categoria not in ["1","2","3"]:
        print(ROJO + "Categoría inválida, ingrese una correcta" + RESET)
        categoria = input("Ingrese la nueva categoría: ")
    if categoria == "1":
        hotel[obtener_posicion(hotel, id_habitacion)][1] = "estandar"
    elif categoria == "2":
        hotel[obtener_posicion(hotel, id_habitacion)][1] = "suite"
    else:
        hotel[obtener_posicion(hotel, id_habitacion)][1] = "premium"

def bloquear_habitacion(id_habitacion):
    """recibe como parámetro un id de habitacion y valida que sea correcto. luego la pone como bloqueada por mantenimiento"""
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print(ROJO + "====ID inválido, ingrese uno correcto====" + RESET)
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    habitacion = hotel[obtener_posicion(hotel, id_habitacion)]
    if habitacion[2] == 2:
        print(ROJO + "No se puede bloquear una habitación reservada" + RESET)
        return
    if habitacion[2] == 0:
        print(ROJO + "La habitación ya está bloqueada" + RESET)
        return
    hotel[obtener_posicion(hotel, id_habitacion)][2] = 0

def habilitar_habitacion(id_habitacion):
    """recibe como parámetro un id de habitacion y valida que sea correcto. Luego la desbloquea y la deja disponible"""
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print(ROJO + "====ID inválido, ingrese uno correcto====" + RESET)
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    habitacion = hotel[obtener_posicion(hotel, id_habitacion)]
    if habitacion[2] != 0:
        print(ROJO + "La habitación no está bloqueada" + RESET)
        return
    hotel[obtener_posicion(hotel, id_habitacion)][2] = 1

def listar_habitaciones_por_estado():
    """lista las habitaciones por estado"""
    estados_hab = ["Bloqueada por mantenimiento", "Disponible", "Reservada"]
    print(VERDE + "======== HABITACIONES POR ESTADO ========" + RESET)
    for estado in range(3):
        print(f"\n{estados_hab[estado]}:")
        encontrado = False
        for hab in hotel:
            if hab[2] == estado:
                print(f"  Habitación {hab[0]} | Categoría: {hab[1]}")
                encontrado = True
        if not encontrado:
            print("  No hay habitaciones en este estado")
    print(VERDE + "=========================================" + RESET)

def consultar_estado(id_habitacion):
    """devuelve el estado de una habitacion"""
    estados = ["Aún no fue reservada", "Confirmada", "Provisoria", "Cancelada"]
    id_habitacion = str(id_habitacion)
    while not id_valido(hotel, id_habitacion):
        print(ROJO + "====ID inválido, ingrese uno correcto====" + RESET)
        id_habitacion = input("Ingrese el ID de la habitación: ")
    id_habitacion = int(id_habitacion)
    habitacion = hotel[obtener_posicion(hotel, id_habitacion)]
    estado = estados[habitacion[5]]
    print(VERDE + f"Habitación {id_habitacion} — Estado: {estado}" + RESET)
    return estado

def informe_general():
    """Devuelve un informe de todas las reservas activas ordenadas por cantidad de noches. 
    En caso de igualdad de noches reservadas, se ordena por orden alfabético del nombre y apellido del huésped.
    Contiene el número de habitación, Categoría, Huésped, Noches, Servicio, Estado de reserva y Precio. """
    servicios = ["Ninguno", "Desayuno", "Spa", "Estacionamiento", "Acceso premium"]
    estados = ["Aún no fue reservada", "Confirmada", "Provisoria", "Cancelada"]
    reservadas = []
    for hab in hotel:
        if hab[2] == 2:
            reservadas.append(hab)
    
    for i in range(len(reservadas)):
        for j in range(i + 1, len(reservadas)):
            if reservadas[i][6] < reservadas[j][6]:
                reservadas[i], reservadas[j] = reservadas[j], reservadas[i]
            elif reservadas[i][6] == reservadas[j][6] and reservadas[i][4] > reservadas[j][4]:
                reservadas[i], reservadas[j] = reservadas[j], reservadas[i]
    
    print("==================== INFORME GENERAL ====================")
    if len(reservadas) == 0:
        print(ROJO + "NO HAY NINGUNA HABITACIÓN RESERVADA" + RESET)
    for hab in reservadas:
        precio = ver_precio(hab[0])
        print("Habitación: " + str(hab[0]) + " | Categoría: " + hab[1] + " | Huésped: " + str(hab[4]) + " | Noches: " + str(hab[6]) + " | Servicio: " + servicios[hab[3]] + " | Estado: " + estados[hab[5]] + " | Precio: $" + str(precio))
    print("=========================================================")

def ocupacion():
    """deuelve un reporte de todas las habitaciones, ocupadas y no, las bloqueadas y el porcentaje de las ocupadas respecto de las libres"""
    total = len(hotel)
    disponibles = 0
    reservadas = 0
    bloqueadas = 0

    for hab in hotel:
        if hab[2] == 1:
            disponibles += 1
        elif hab[2] == 2:
            reservadas += 1
        elif hab[2] == 0:
            bloqueadas += 1

    porcentaje = (reservadas / total) * 100

    print(VERDE + "========== REPORTE DE OCUPACIÓN ==========" + RESET)
    print(f"Total de habitaciones:              {total}")
    print(f"Habitaciones disponibles:           {disponibles}")
    print(f"Habitaciones reservadas:            {reservadas}")
    print(f"Habitaciones bloqueadas:            {bloqueadas}")
    print(f"Porcentaje de ocupación:            {porcentaje}%")
    print(VERDE + "==========================================" + RESET)

def reporte_por_categoria():
    """devuelve un reporte de cuantas habitaciones hay reservadas para cada categoria, 
    cuantas noches hay acumuladas, y el reporte total de venta"""
    categorias = ["estandar", "suite", "premium"]
    
    print(VERDE + "======== REPORTE POR CATEGORÍA ========" + RESET)
    for categoria in categorias:
        reservadas = 0
        noches = 0
        total = 0
        for hab in hotel:
            if hab[1] == categoria and hab[2] == 2:
                reservadas += 1
                noches += hab[6]
                total += ver_precio(hab[0])
        print(f"Categoría: {categoria}")
        print(f"  Habitaciones reservadas: {reservadas}")
        print(f"  Noches acumuladas:       {noches}")
        print(f"  Importe total:           ${total}")
        print("---------------------------------------")
    print(VERDE + "=======================================" + RESET)


