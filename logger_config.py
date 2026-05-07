############################
# Archivo: logger_config.py
# Descripción: Configuración del Logger para registrar eventos y errores en el sistema.
############################
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

#############################
#Excepciones personalizadas para validación de datos
#############################

#Se dispara si el ID o Telefono no cumplen el formato
class ErrorValidacionDatos(Exception):
   pass

#Se dispara si algo falla al intentar confirmar una reserva
class ErrorOperacionReserva(Exception):    
    pass

# Función para registrar eventos en el log. 
# Centraliza el manejo de logs para facilitar su uso en todo el proyecto.
def registrar_evento(mensaje, nivel="info"):
    if nivel == "error":
        logging.error(mensaje)
    else:
        logging.info(mensaje)


#Clase base para errores del sistema Software FJ
class ErrorValidacionFJ(Exception):   
    def __init__(self, mensaje):
        self.mensaje = mensaje  # Aquí definimos el atributo 'mensaje'
        super().__init__(self.mensaje)



# Excepciones específicas para validaciones comunes en el sistema
#Se lanza cuando un campo (Documento/Teléfono) contiene letras o símbolos
class ErrorDatoNoNumerico(ErrorValidacionFJ):    
    def __init__(self, campo, valor):
        self.mensaje = f"Error Critico: El {campo} '{valor}' no es un dato numerico válido."
        super().__init__(self.mensaje)


#Se lanza cuando el teléfono tiene más de 10 dígitos o no es numérico
#Se lanza cuando un parámetro obligatorio falta
class ErrorCampoVacio(ErrorValidacionFJ):    
    def __init__(self, campo):
        self.mensaje = f"Fallo en Registro: El parámetro '{campo}' es obligatorio."
        super().__init__(self.mensaje)