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

######################################
# Función para limpiar los campos de entrada
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
    entry_cantidad.insert(0, "1")

######################################
# Funciones para actualizar los detalles del servicio y 
# calcular el costo del servicio al seleccionar un detalle
######################################

def actualizar_detalles(event):
    opciones = {
        "Equipo": ["PC Gamer", "Laptop Oficina", "Silla Ergonómica"],
        "Sala": ["Reserva de Sala", "Sala de Juntas", "Sala de Capacitación"],
        "Asesoria": ["Legal", "Técnica", "Contable"]
    }
    combo_detalle.config(values=opciones.get(combo_servicio.get(), []))

def al_seleccionar_detalle(event):
    precios = {
        "PC Gamer": 20000, "Laptop Oficina": 10000, "Silla Ergonómica": 5000,
        "Legal": 50000, "Técnica": 30000, "Contable": 40000, 
        "Reserva de Sala": 15000, "Sala de Juntas": 20000, "Sala de Capacitación": 25000
    }
    precio = precios.get(combo_detalle.get(), 0)
    # Bloqueo únicamente del valor del servicio
    entry_costo_servicio.config(state="normal")
    entry_costo_servicio.delete(0, tk.END)
    entry_costo_servicio.insert(0, str(precio))
    entry_costo_servicio.config(state="readonly")

######################################
# Funciones para procesar la reserva, incluyendo validaciones de entrada, 
# cálculo del costo total, y actualización de la tabla de reservas
######################################

def procesar_reserva():
    doc = entry_num_doc.get().strip()
    nom = entry_nombre.get().strip()
    tel = entry_telefono.get().strip()
    tipo = combo_tipo_doc.get()
    det = combo_detalle.get()
    costo = entry_costo_servicio.get().strip()
    cant = entry_cantidad.get().strip()

    # Validaciones
    if not doc.isdigit():
        registrar_log(f"FALLO: Documento '{doc}' no numérico", "WARNING")
        return messagebox.showerror("Error", "El documento debe ser numérico.")
    if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", nom):
        registrar_log(f"FALLO: Nombre '{nom}' inválido", "WARNING")
        return messagebox.showerror("Error", "El nombre solo debe contener letras.")
    if len(tel) != 10 or not tel.isdigit():
        return messagebox.showerror("Error", "El teléfono debe tener 10 números.")

    try:
        # Cálculo: Costo Unitario x Cantidad
        total_numerico = float(costo) * int(cant)
        f_ini = entry_fecha.get()
        f_fin = (datetime.strptime(f_ini, "%Y-%m-%d") + timedelta(days=int(cant)-1)).strftime("%Y-%m-%d")
        
        estado = "Finalizado" if combo_servicio.get() == "Asesoria" else "En Uso"
        doc_full = f"{tipo} {doc}"
        
        tabla.insert("", "end", values=(f_ini, doc_full, nom, det, f"${total_numerico:,.2f}", f_fin, estado))
        
        registrar_log(f"EXITO - Registro: {nom} | Total: ${total_numerico:,.2f}")
        guardar_datos()
        actualizar_total_recaudado()
        limpiar_campos() # Borra los datos después de registrar
        messagebox.showinfo("Éxito", "Registro completado.")
    except Exception as e:
        registrar_log(f"ERROR: {e}", "ERROR")


######################################
# Función para registrar la devolución de un servicio, actualizando el estado y 
# recalculando el total si es necesario
######################################
def registrar_devolucion():
    seleccion = tabla.selection()
    if not seleccion: return
    
    # Usa la fecha del campo de texto para calcular la entrega
    fecha_entrega_str = entry_fecha.get().strip()
    try:
        f_entrega = datetime.strptime(fecha_entrega_str, "%Y-%m-%d")
    except:
        return messagebox.showerror("Error", "Formato de fecha inválido.")

    for item in seleccion:
        v = list(tabla.item(item)['values'])
        if v[6] == "En Uso":
            f_ini = datetime.strptime(v[0], "%Y-%m-%d")
            # Diferencia de días + 1 para cobro inclusivo
            dias_reales = (f_entrega - f_ini).days + 1
            
            if dias_reales < 1: continue

            # Precios base para el recalcular el total real
            precios = {
                "PC Gamer": 20000, "Laptop Oficina": 10000, "Silla Ergonómica": 5000,
                "Legal": 50000, "Técnica": 30000, "Contable": 40000, 
                "Reserva de Sala": 15000, "Sala de Juntas": 20000, "Sala de Capacitación": 25000
            }
            costo_u = precios.get(v[3], 0)
            
            v[4] = f"${(costo_u * dias_reales):,.2f}"
            v[5] = fecha_entrega_str
            v[6] = "Devuelto"
            tabla.item(item, values=v)
            
    guardar_datos()
    actualizar_total_recaudado()
    messagebox.showinfo("Éxito", "Estado actualizado.")


######################################
# Función para eliminar un registro de la tabla
######################################

def eliminar_registro():
    seleccion = tabla.selection()
    if not seleccion: return
    if messagebox.askyesno("Confirmar", "¿Eliminar registro?"):
        for item in seleccion:
            tabla.delete(item)
        guardar_datos()
        actualizar_total_recaudado()

##############################
# Configuración de la ventana principal y creación de los widgets
##############################

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Software FJ - Gestión de Reservas")
root.geometry("950x850")

# Crear un marco para los datos del cliente
f_cli = ttk.LabelFrame(root, text=" Datos de Cliente ", padding=10)
f_cli.pack(fill="x", padx=20, pady=10)

# Crear los campos de entrada para los datos del cliente
ttk.Label(f_cli, text="Tipo Doc:").grid(row=0, column=0, sticky="w")
combo_tipo_doc = ttk.Combobox(f_cli, values=["CC", "RUT", "CE"], width=7, state="readonly")
combo_tipo_doc.grid(row=0, column=1, sticky="w")

# Campo de número de documento
ttk.Label(f_cli, text="Documento:").grid(row=0, column=2, sticky="w", padx=(10,0))
entry_num_doc = ttk.Entry(f_cli); entry_num_doc.grid(row=0, column=3, sticky="ew")

# Campo de nombre del cliente
ttk.Label(f_cli, text="Nombre:").grid(row=1, column=0, sticky="w", pady=5)
entry_nombre = ttk.Entry(f_cli); entry_nombre.grid(row=1, column=1, columnspan=3, sticky="ew")
ttk.Label(f_cli, text="Teléfono (10 dígitos):").grid(row=2, column=0, sticky="w")

# Campo de teléfono del cliente
entry_telefono = ttk.Entry(f_cli); entry_telefono.grid(row=2, column=1, columnspan=3, sticky="ew")
f_cli.columnconfigure(3, weight=1)


# Crear un marco para la configuración y reserva de servicios

f_res = ttk.LabelFrame(root, text=" Configuración y Reserva ", padding=10)
f_res.pack(fill="x", padx=20)

# Campos para seleccionar el servicio, detalle, costo unitario, cantidad/días y fecha
ttk.Label(f_res, text="Servicio:").grid(row=0, column=0, sticky="w")

# Combobox para seleccionar el tipo de servicio, con un evento que actualiza los detalles disponibles
combo_servicio = ttk.Combobox(f_res, values=["Equipo", "Sala", "Asesoria"], state="readonly")
combo_servicio.grid(row=0, column=1, sticky="ew"); combo_servicio.bind("<<ComboboxSelected>>", actualizar_detalles)

# Combobox para seleccionar el detalle del servicio, que se actualiza según el servicio seleccionado
ttk.Label(f_res, text="Detalle:").grid(row=1, column=0, sticky="w", pady=5)
combo_detalle = ttk.Combobox(f_res, state="readonly")
combo_detalle.grid(row=1, column=1, sticky="ew"); combo_detalle.bind("<<ComboboxSelected>>", al_seleccionar_detalle)

# Campo de costo unitario
ttk.Label(f_res, text="Costo Unit:").grid(row=2, column=0, sticky="w")
entry_costo_servicio = ttk.Entry(f_res, state="readonly")
entry_costo_servicio.grid(row=2, column=1, sticky="ew")

# Campo de cantidad/días
ttk.Label(f_res, text="Días/Cant:").grid(row=3, column=0, sticky="w", pady=5) # Etiqueta para cantidad o días, dependiendo del servicio seleccionado
entry_cantidad = ttk.Entry(f_res); entry_cantidad.insert(0, "1"); entry_cantidad.grid(row=3, column=1, sticky="ew") # Campo de entrada para la cantidad o días, con un valor predeterminado de 1
ttk.Label(f_res, text="Fecha (AAAA-MM-DD):").grid(row=4, column=0, sticky="w")# Etiqueta para la fecha de inicio de la reserva, con un formato específico
entry_fecha = ttk.Entry(f_res)
entry_fecha.insert(0, datetime.now().strftime("%Y-%m-%d"))# Campo de entrada para la fecha, con un valor predeterminado de la fecha actual en formato AAAA-MM-DD
entry_fecha.grid(row=4, column=1, sticky="ew")
f_res.columnconfigure(1, weight=1)

# Crear un marco para los botones de acción
f_btns = tk.Frame(root); f_btns.pack(pady=15)
ttk.Button(f_btns, text="Registrar", command=procesar_reserva).pack(side="left", padx=5)
ttk.Button(f_btns, text="Marcar Devolución", command=registrar_devolucion).pack(side="left", padx=5)
ttk.Button(f_btns, text="Eliminar Registro", command=eliminar_registro).pack(side="left", padx=5)

# Crear la tabla para mostrar las reservas
columnas = ("F", "D", "C", "S", "T", "Fi", "E")
tabla = ttk.Treeview(root, columns=columnas, show="headings", height=12)
for c, n in zip(columnas, ["Fecha", "Doc", "Cliente", "Servicio", "Total", "Fin", "Estado"]):
    tabla.heading(c, text=n); tabla.column(c, width=120, anchor="center")
tabla.pack(fill="both", expand=True, padx=20)

# Etiqueta para mostrar el total recaudado
lbl_total_recaudado = ttk.Label(root, text="Total Recaudado: $0.00", font=("Arial", 12, "bold"))
lbl_total_recaudado.pack(pady=10)

# Cargar datos al iniciar la aplicación y actualizar el total recaudado
cargar_datos()
actualizar_total_recaudado()
root.mainloop()
