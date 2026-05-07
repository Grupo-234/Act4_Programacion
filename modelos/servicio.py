
# Clase que representa un servicio ofrecido por Software FJ
class Servicio:
    def __init__(self, nombre_servicio, precio_base):
        self._nombre_servicio = nombre_servicio
        self.precio_base = precio_base


# Clase que representa el servicio de reserva de sala, hereda de Servicio
class ReservaSala(Servicio):
    def __init__(self, costo_personalizado):
        super().__init__("Reserva de Sala", costo_personalizado)
    def calcular_precio(self, horas):
        return self.precio_base * horas

# Clase que representa el servicio de alquiler de equipo, hereda de Servicio
class AlquilerEquipo(Servicio):
    def __init__(self, detalle_equipo, costo_personalizado):
        super().__init__(f"Alquiler de {detalle_equipo}", costo_personalizado)

    def calcular_precio(self, cantidad):
        return self.precio_base * cantidad