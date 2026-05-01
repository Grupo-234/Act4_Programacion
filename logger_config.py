import logging

# Configuración del Logger
# 'level=logging.INFO' permite capturar tanto errores como eventos positivos.
# 'filemode='a'' (append) asegura que el historial no se borre al reiniciar el programa.
logging.basicConfig(
    filename='registro_eventos.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='a' 
)
############################
#Excepciones Personalizadas
#Manejo de errores especificos
############################
class ErrorValidacionDatos(Exception):
    """Se dispara si el ID o Teléfono no cumplen el formato."""
    pass

class ErrorOperacionReserva(Exception):
    """Se dispara si algo falla al intentar confirmar una reserva."""
    pass

def registrar_evento(mensaje, nivel="info"):
    """Centraliza los reportes. Así, si mañana queremos cambiar 
    el formato del log, solo editamos aquí."""
    if nivel == "error":
        logging.error(mensaje)
    else:
        logging.info(mensaje)