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
 
###################################################
#Metodo Abstracto. Metodo obligatorio para quienes hereden de esta clase
###################################################
 
    @abstractmethod
    def mostrar_perfil(self): 
        pass

###################################################
# Validaciones específicas para los campos de la entidad
###################################################

    def _validar_documento(self, valor):
        # Implementamos la lógica de "Solo números"
        if not str(valor).isdigit():
            msg = f"Error Crítico: El documento '{valor}' no es numérico."
            registrar_evento(msg, nivel="error")
            raise ErrorValidacionDatos(msg)
        return valor