##============================
#Importamos la clase base EntidadPersona
##############################

from abc import ABC, abstractmethod
# Importamos las herramientas de infraestructura
from logger_config import registrar_evento, ErrorValidacionDatos


#==================================
# Clase Cliente
# Hereda de EntidadPersona
# Maneja la información del cliente
#==================================

# Creamos una clase abstracta para representar a personas en general
class EntidadPersona(ABC): # Clase Abstracta
    def __init__(self, tipo_doc, num_doc, nombre, telefono, correo=None):
        self._tipo_doc = tipo_doc
        # Aquí aplicamos las validaciones que discutimos
        self._num_doc = self._validar_documento(num_doc)
        self._nombre = nombre
        self._telefono = self._validar_telefono(telefono)
        self._correo = correo
        self._estado = "Activo"



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



