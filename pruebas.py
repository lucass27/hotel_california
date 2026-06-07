from funciones import *

def ver_estadoReserva_individual(piso,numero):
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

hola = ver_estadoReserva_individual(6,610)
print(hola)