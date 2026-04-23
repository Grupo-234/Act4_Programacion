##Componente práctico - Prácticas simuladas
##Programacion orientada a objetos
##Grupo: 213023_234
#Sistema Integral de Gestión de Clientes, Servicios y Reservas

from abc import ABC, abstractmethod
import logging
from datetime import datetime

# Configuración del archivo de logs 
logging.basicConfig(
    filename='registro_eventos.log', 
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 1. Clase Abstracta que representa entidades generales
class EntidadPersona(ABC):
    def __init__(self, tipo_doc, num_doc, nombre_completo, telefono, correo=None):
        # Aplicamos encapsulación con atributos protegidos
        self._tipo_doc = tipo_doc
        self._num_doc = self._validar_documento(num_doc)
        self._nombre_completo = nombre_completo
        self._telefono = self._validar_telefono(telefono)
        self._correo = self._validar_correo(correo)
        self._estado = "Activo"
        self._fecha_registro = datetime.now()

    # Métodos de validacion documento de identidad
    def _validar_documento(self, valor):
        if not str(valor).isdigit():
            error_msg = f"ID inválido: {valor}. Solo se permiten números."
            logging.error(error_msg) # Registro en el log
            raise ValueError(error_msg)
        return valor

    #Validacion de telefono: maximo 10 digitos numericos
    def _validar_telefono(self, valor):
        if len(str(valor)) > 10 or not str(valor).isdigit():
            error_msg = f"Teléfono inválido: {valor}. Máximo 10 dígitos numéricos."
            logging.error(error_msg)
            raise ValueError(error_msg)
        return valor

    #Validacion de correo: debe contener "@" y "."
    def _validar_correo(self, valor):
        if valor and ("@" not in valor or "." not in valor):
            error_msg = f"Formato de correo incorrecto: {valor}."
            logging.error(error_msg)
            raise ValueError(error_msg)
        return valor

    @abstractmethod
    def mostrar_perfil(self):
        """Obliga a las clases hijas a implementar su propia descripción"""
        pass

