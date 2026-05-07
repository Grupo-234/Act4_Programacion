#########################
# importaciones necesarias para el funcionamiento del módulo de reserva
########################
from logger_config import registrar_evento, ErrorOperacionReserva


#########################
#Definición de la clase Reserva, que representa una reserva realizada por un cliente para un servicio específico.
########################
class Reserva:
    def __init__(self, cliente, servicio, cantidad, fecha):
        # Validamos que la cantidad sea un entero positivo
        if not isinstance(cantidad, int) or cantidad <= 0:
            msg = f"Fallo en Reserva: Cantidad '{cantidad}' no valida. Debe ser un entero positivo."
            registrar_evento(msg, nivel="error")
            raise ErrorOperacionReserva(msg)
        
        self.cliente = cliente # Referencia al cliente que realiza la reserva
        self.servicio = servicio # Referencia al servicio que se está reservando
        self.cantidad = cantidad # Cantidad de unidades del servicio que se están reservando
        self.fecha = fecha        # Fecha de la reserva
        self.total = servicio.calcular_precio(cantidad) # Cálculo del precio total de la reserva basado en el servicio y la cantidad