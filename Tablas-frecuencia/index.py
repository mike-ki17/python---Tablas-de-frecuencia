import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, Canvas, Scrollbar

import csv
import subprocess
import margenError
import limpiardb
# import graficos

def mostrarTabla() :
    tabla2.pack()
    boton_er.pack()
    # boton_graficos.pack()



    with open('./tabla_frecuencias_agrupado.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Obtener el encabezado del CSV
        tabla2["columns"] = header
        tabla2.heading("#0", text="ID")  # Columna de ID
        for col in header:
            tabla2.heading(col, text=col)
            tabla2.column(col, width=100)  # Ancho de las columnas
            
        for id, row in enumerate(reader, 1):
            tabla2.insert("", "end", text=str(id), values=row)


def mostrarElementos():
    etiqueta2.pack()
    labelIntervalos.pack()
    Nintervalos.pack()  
    boton_cargar_2.pack()
    tabla.pack(padx=10, pady=5)
    # espacio_vertical.pack()


def obtenerIntervalos():
    Intervalos = Nintervalos.get()
    return Intervalos

def abrir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.csv"), ("Todos los archivos", "*.*")])
    if archivo:
        print(f"Archivo seleccionado: {archivo}")
        mostrarElementos()
        
        # Limpiar cualquier fila existente en el Treeview
        for fila in tabla.get_children():
            tabla.delete(fila)
        
        with open(archivo, 'r') as file:
            reader = csv.reader(file)


             # === Obtener el numero de columnas ===
            column_count = len(next(reader))
            if column_count > 2:
                melt_df = limpiardb.melt_DB(archivo)

            else:

                header = next(reader)  # Obtener el encabezado del CSV
                tabla["columns"] = header
                tabla.heading("#0", text="ID")  # Columna de ID
                for col in header:
                    tabla.heading(col, text=col)
                    tabla.column(col, width=100)  # Ancho de las columnas
                
                for id, row in enumerate(reader, 1):
                    tabla.insert("", "end", text=str(id), values=row)

                programa_externo = "ndatos.py"
                subprocess.run(["python3", programa_externo, archivo])
    return archivo



def abrir_archivo_2():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.csv"), ("Todos los archivos", "*.*")])
    if archivo:
        print(f"Archivo seleccionado: {archivo}")
        tabla.pack(padx=10, pady=5)
        
        # Limpiar cualquier fila existente en el Treeview
        for fila in tabla.get_children():
            tabla.delete(fila)
        
        with open(archivo, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Obtener el encabezado del CSV
            tabla["columns"] = header
            tabla.heading("#0", text="ID")  # Columna de ID
            for col in header:
                tabla.heading(col, text=col)
                tabla.column(col, width=100)  # Ancho de las columnas
            
            for id, row in enumerate(reader, 1):
                tabla.insert("", "end", text=str(id), values=row)

        K = obtenerIntervalos()
        programa_externo = "datosAgrupados.py"
        subprocess.run(["python3", programa_externo, archivo, K])

        mostrarTabla()
    
    return archivo


def MostrarDataos ():
    # return margenError.ErrorRelativo(abrir_archivo(), abrir_archivo_2)
    mostrar_ventana_emergente()
    
# def MostrarGraficos ():
#     ventana_emergente_graficos = tk.Toplevel(ventana)
#     ventana_emergente_graficos.title("graficos estadisticos")
#     graficos.showGraficos()
    
    
    




def mostrar_ventana_emergente():
    ventana_emergente = tk.Toplevel(ventana)
    ventana_emergente.title("Datos estadisticos")
    
    etiqueta = tk.Label(ventana_emergente, text="Datos Estadisticos de tu tabla agrupada")
    etiqueta.pack(padx=20, pady=20)
    errorR = tk.Label(ventana_emergente, text=f'Error relativo de la tabla: {margenError.ErrorRelativo()}', padx=10, pady=10)
    errorR.pack()
    


    
ventana = tk.Tk()
ventana.geometry("600x750")
ventana.title("Tabla de frecuencias")



etiqueta = tk.Label(ventana, text="Ingresa la base de datos inicial", padx=10, pady=10)
etiqueta.pack()

boton_cargar = tk.Button(ventana, text="Cargar Archivo", command=abrir_archivo, padx=20, pady=5)
boton_cargar.pack()

etiqueta2 = tk.Label(ventana, text="tabla de frecuencia para tados agrupados", padx=10, pady=10)

labelIntervalos = tk.Label(ventana, text="Numero de intervalos:")
Nintervalos = tk.Entry(ventana, width=5)

boton_cargar_2 = tk.Button(ventana, text="Cargar Archivo", command=abrir_archivo_2, padx=20, pady=5)

tabla = ttk.Treeview(ventana)

# espacio_vertical = tk.Label(ventana, text="", height=2)

boton_er = tk.Button(ventana, text="Mostrar datos de la tabla", command=MostrarDataos, padx=20, pady=5)
# boton_graficos = tk.Button(ventana, text="Mostrar graficos", command=MostrarGraficos, padx=20, pady=5)

tabla2 = ttk.Treeview(ventana)




ventana.mainloop()
