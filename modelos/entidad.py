##============================
#Importamos la clase base EntidadPersona
##############################

from abc import ABC, abstractmethod
from logger_config import registrar_evento, ErrorValidacionDatos
from logger_config import ErrorCampoVacio, ErrorDatoNoNumerico
from logger_config import registrar_evento, ErrorValidacionFJ


#==================================
# Clase Cliente
# Hereda de EntidadPersona
# Maneja la información del cliente
#==================================

# Creamos una clase abstracta para representar a personas en general
class EntidadPersona(ABC): # Clase Abstracta
    def __init__(self, tipo_doc, num_doc, nombre, telefono, correo=None):
        self._tipo_doc = tipo_doc      
        self._num_doc = self._validar_documento(num_doc)
        self._nombre = nombre
        self._telefono = self._validar_telefono(telefono)
        self._correo = correo
        self._estado = "Activo"

    
    @abstractmethod
    def mostrar_perfil(self): 
        """Este método es obligatorio para quienes hereden de aquí"""
        pass

    # Método para validar el número de documento
    def _validar_documento(self, valor):
        # Implementamos la lógica de "Solo números"
        if not str(valor).isdigit():
            msg = f"Error Critico: El documento '{valor}' no es numerico."
            registrar_evento(msg, nivel="error")
            raise ErrorValidacionDatos(msg)
        return valor

    # Método para validar el teléfono
    def _validar_telefono(self, valor):
        # Implementamos la lógica de "Solo números y máximo 10 dígitos"
        if not (str(valor).isdigit() and len(str(valor)) <= 10):
            msg = f"Error Crítico: Teléfono '{valor}' inválido (Máx 10 dígitos)."
            registrar_evento(msg, nivel="error")
            raise ErrorValidacionDatos(msg)
        return valor


###############################
#Clase Cliente que hereda de EntidadPersona
###############################
class Cliente:
    def __init__(self, nombre, documento, telefono):
        self.nombre = nombre        # Llama al setter de nombre
        self.documento = documento  # Llama al setter de documento
        self.telefono = telefono    # Llama al setter de telefono

    @property # Decorador para el getter del documento
    def documento(self):
        return self._documento

    @documento.setter # Decorador para el setter del documento
    def documento(self, valor):
        if not valor:
            raise ErrorCampoVacio("Documento")
        if not valor.isdigit():
            raise ErrorDatoNoNumerico("Documento", valor)
        self._documento = valor

    @property # Decorador para el getter del telefono
    def telefono(self):
        return self._telefono

    @telefono.setter # Decorador para el setter del telefono    
    def telefono(self, valor):
        if not valor.isdigit():
            raise ErrorDatoNoNumerico("Telefono", valor)
        
        if len(valor) != 10:
            # Enviamos el texto directamente a la clase base
            raise ErrorValidacionFJ(f"Telefono '{valor}' inválido (Debe tener 10 digitos)")
            
        self._telefono = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ErrorCampoVacio("Nombre")
        self._nombre = valor



