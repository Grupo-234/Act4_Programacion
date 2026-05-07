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


class Cliente(EntidadPersona):

    # Constructor de la clase
    # Recibe los datos principales del cliente
    def __init__(self, nombre, cedula, telefono, correo, direccion):

        # Guarda el nombre del cliente
        self._nombre = nombre

        # Valida que la cédula tenga solo números
        if not cedula.isdigit():
            raise ValueError("La cédula debe contener solo números")

        # Guarda la cédula
        self._cedula = cedula

        # Valida longitud del teléfono
        if len(telefono) < 7:
            raise ValueError("Teléfono inválido")

        # Guarda teléfono
        self._telefono = telefono

        # Valida correo
        if "@" not in correo:
            raise ValueError("Correo inválido")

        # Guarda correo
        self._correo = correo

        # Valida dirección
        if direccion == "":
            raise ValueError("La dirección no puede estar vacía")

        # Guarda dirección
        self._direccion = direccion

    #==================================
    # Método para mostrar información
    #==================================
    def mostrar_perfil(self):

        # Retorna la información organizada
        return f"""
        Nombre: {self._nombre}
        Cédula: {self._cedula}
        Teléfono: {self._telefono}
        Correo: {self._correo}
        Dirección: {self._direccion}
        """

    #==================================
    # Método para actualizar teléfono
    #==================================
    def actualizar_telefono(self, nuevo_telefono):

        # Valida longitud mínima
        if len(nuevo_telefono) < 7:
            raise ValueError("Teléfono inválido")

        # Actualiza teléfono
        self._telefono = nuevo_telefono

    #==================================
    # Método para actualizar correo
    #==================================
    def actualizar_correo(self, nuevo_correo):

        # Valida correo
        if "@" not in nuevo_correo:
            raise ValueError("Correo inválido")

        # Actualiza correo
        self._correo = nuevo_correo

    #==================================
    # Método para actualizar dirección
    #==================================
    def actualizar_direccion(self, nueva_direccion):

        # Valida dirección
        if nueva_direccion == "":
            raise ValueError("La dirección no puede estar vacía")

        # Actualiza dirección
        self._direccion = nueva_direccion

    #==================================
    # Método resumen
    #==================================
    def resumen_cliente(self):

        # Retorna información corta del cliente
        return f"{self._nombre} - {self._correo}"



