
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

