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
    filename='registro_eventos.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True
)