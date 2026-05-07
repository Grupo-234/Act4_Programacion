##########################
# Importamos las librerías necesarias para la aplicación
##########################

import tkinter as tk # Interfaz gráfica de usuario
from tkinter import ttk, messagebox # ttk para estilos de widgets, messagebox para mostrar mensajes emergentes
from datetime import datetime, timedelta # datetime para manejar fechas y horas, timedelta para realizar operaciones con fechas
import re # re para expresiones regulares, útil para validar entradas de usuario
import logging # logging para registrar eventos y errores en la aplicación
import csv # csv para manejar archivos CSV, útil para guardar y cargar datos de usuarios
import os # os para interactuar con el sistema operativo, como verificar la existencia de archivos o crear directorios

##########################
# Configuración del logging para registrar eventos y errores
##########################
logging.basicConfig(
    filename='registro_eventos.log', # Archivo donde se guardarán los registros de eventos
    level=logging.INFO, # Nivel de logging, INFO para registrar eventos informativos, ERROR para registrar errores
    format='%(asctime)s - %(levelname)s - %(message)s', # Formato del mensaje de logging, incluye la fecha y hora, el nivel de logging y el mensaje
    datefmt='%Y-%m-%d %H:%M:%S', # Formato de la fecha y hora en los registros
    force=True # Forzar la configuración del logging, útil para evitar conflictos con configuraciones previas de logging en otros módulos o bibliotecas
)

######################################
# Función para registrar eventos en el archivo de logging
######################################
def registrar_log(mensaje, nivel="INFO"): 
    if nivel == "INFO": logging.info(mensaje) # Registrar un evento informativo
    elif nivel == "ADVERTENCIA": logging.warning(mensaje) # Registrar un evento de advertencia
    elif nivel == "ERROR": logging.error(mensaje) # Registrar un evento de error
    for handler in logging.root.handlers:
        handler.flush()
    
######################################
# Función para cargar datos desde un archivo CSV y llenar la tabla de reservas
######################################
def guardar_datos():
    try:
        with open('reservas.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for item in tabla.get_children():
                writer.writerow(tabla.item(item)['values'])
    except Exception as e:
        registrar_log(f"SISTEMA - Error al guardar: {e}", "ERROR")