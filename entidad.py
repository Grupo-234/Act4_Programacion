##################################################
# Importamos las herramientas de infraestructura
##################################################
from abc import ABC, abstractmethod
from logger_config import registrar_evento, ErrorValidacionDatos


###################################################
#Definicion de la clase base para las entidades de personas
###################################################
class EntidadPersona(ABC):
    def __init__(self, tipo_doc, num_doc, nombre, telefono, correo=None):
        self._tipo_doc = tipo_doc
        # Aquí aplicamos las validaciones que discutimos
        self._num_doc = self._validar_documento(num_doc)
        self._nombre = nombre
        self._telefono = self._validar_telefono(telefono)
        self._correo = correo
        self._estado = "Activo"