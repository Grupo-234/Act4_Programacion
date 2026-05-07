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


###########################
# Métodos para gestionar la reserva
############################
# Método para confirmar la reserva, que genera un mensaje de log con los detalles de la reserva y confirma el proceso.
    def confirmar_reserva(self):
        """Genera el mensaje para el log y confirma el proceso."""
        resumen_log = (
            f"Proceso Exitoso - Cliente: {self.cliente._nombre} | "
            f"Servicio: {self.servicio._nombre_servicio} | Total: {self.total}"
        )
        registrar_evento(resumen_log, nivel="info")
        return "Reserva procesada y registrada exitosamente."
    
    # Método para representar la reserva como una cadena de texto, mostrando los detalles de la reserva.
    def __str__(self):
        
        return (
            f"\n==============================="
            f"\n       COMPROBANTE DE RESERVA  "
            f"\n==============================="
            f"\nFecha: {self.fecha}"
            f"\nCliente: {self.cliente._nombre} ({self.cliente._tipo_doc}: {self.cliente._num_doc})"
            f"\nServicio: {self.servicio._nombre_servicio}"
            f"\nCantidad: {self.cantidad}"
            f"\nTotal a Pagar: ${self.total}"
            f"\n===============================\n"
        )