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
