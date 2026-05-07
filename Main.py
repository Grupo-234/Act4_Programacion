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
        with open('reservas.csv', 'w', newline='', encoding='utf-8') as file: # Abrir el archivo CSV en modo escritura
            writer = csv.writer(file) # Crear un objeto writer para escribir en el archivo CSV
            for item in tabla.get_children(): # Iterar sobre los elementos de la tabla de reservas
                writer.writerow(tabla.item(item)['values']) # Escribir los valores de cada elemento de la tabla en el archivo CSV
    except Exception as e:
        registrar_log(f"SISTEMA - Error al guardar: {e}", "ERROR") # Registrar un error si ocurre una excepción al guardar 


######################################
# Función para cargar datos desde un archivo CSV y llenar la tabla de reservas
######################################
def cargar_datos():
    if os.path.exists('reservas.csv'): # Verificar si el archivo CSV existe antes de intentar cargar los datos
        try:
            with open('reservas.csv', 'r', encoding='utf-8') as file: # Abrir el archivo CSV en modo lectura
                reader = csv.reader(file) # Crear un objeto reader para leer el archivo CSV
                for row in reader:
                    tabla.insert("", "end", values=row)
        except Exception as e:
            registrar_log(f"SISTEMA - Error al cargar: {e}", "ERROR") # Registrar un error si ocurre una excepción al cargar los datos

######################################
# Función para actualizar el total recaudado sumando los valores de la columna "Total"
######################################
def actualizar_total_recaudado():
    total = 0.0
    for item in tabla.get_children():
        valores = tabla.item(item)['values']
        try:
            val = str(valores[4]).replace('$', '').replace(',', '')
            total += float(val)
        except: continue
    lbl_total_recaudado.config(text=f"Total Recaudado: ${total:,.2f}")

'''######################################
# 
######################################
def limpiar_campos():
    entry_num_doc.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    # Habilitar temporalmente para limpiar campo bloqueado
    entry_costo_servicio.config(state="normal")
    entry_costo_servicio.delete(0, tk.END)
    entry_costo_servicio.config(state="readonly")
    combo_tipo_doc.set('')
    combo_servicio.set('')
    combo_detalle.set('')
    entry_cantidad.delete(0, tk.END)
    entry_cantidad.insert(0, "1")'''