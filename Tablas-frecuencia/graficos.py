import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
from scipy.stats import norm

# Genera datos de ejemplo (reemplaza esto con tus datos)
# datos = np.random.normal(loc=0, scale=1, size=1000)  # Media=0, Desviación Estándar=1

# Calcula la media y la desviación estándar de tus datos


# # Crea un rango de valores para el eje x basado en la distribución normal
# x = np.linspace(media - 3 * desviacion_estandar, media + 3 * desviacion_estandar, 100)

# # Calcula la PDF de la distribución normal para el rango de valores
# pdf = norm.pdf(x, media, desviacion_estandar)

# # Crea el gráfico de la distribución normal
# plt.plot(x, pdf, label='Distribución Normal', color='blue')

# # Personaliza el gráfico
# plt.title('Distribución Normal')
# plt.xlabel('Valores')
# plt.ylabel('Densidad de Probabilidad')
# plt.legend()
# plt.grid(True)

# # Muestra el gráfico
# plt.show()



bd = './csv/datos_estadistica.csv'
bdgrup = './tabla_frecuencias_agrupado.csv'
bd_inicial = './csv/bd_estadistica.csv'
df = pd.read_csv(bd)
dfgrup = pd.read_csv(bdgrup)

df2 = pd.read_csv(bd_inicial)
column1Df = df2.iloc[:, 0]
media = round(column1Df.mean(), 2)
# desviacion_estandar = ndatos.mdd[3]
print(media)


root = tk.Tk()
root.title("Gráfico de Matplotlib en Tkinter")

frame = tk.Frame(root)
frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)





def showGraficos ():
    

   ancho_figura = 3
   alto_figura = 2

   fig1, ax1 = plt.subplots(figsize=(ancho_figura, alto_figura))
   ax1.bar(df['X'], df['F'])
   ax1.set_title('Frecuencia')
   ax1.set_xlabel('Calificaciones')
   ax1.set_ylabel('Frecuencia')
   ax1.grid(True, linestyle='--', alpha=0.7)


   fig2, ax2 = plt.subplots(figsize=(ancho_figura, alto_figura))
   ax2.pie(dfgrup['H%'], labels=dfgrup['Clases'], autopct='%1.1f%%')
   ax2.set_title('Porcentaje de Frecuencias')
   


   fig3, ax3 = plt.subplots(figsize=(ancho_figura, alto_figura))
   ancho_barra = 2
   ax3.set_title('Frecuencia')
   ax3.bar(dfgrup['X'], dfgrup['F'], width=ancho_barra)
   ax3.set_xlabel('Calificaciones')
   ax3.set_ylabel('Frecuencia')
   ax3.grid(True, linestyle='--', alpha=0.7)


   canvas = FigureCanvasTkAgg(fig1, master=frame)
   canvas_widget = canvas.get_tk_widget()
   canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


   canvas2 = FigureCanvasTkAgg(fig2, master=frame)
   canvas_widget2 = canvas2.get_tk_widget()
   canvas_widget2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


   canvas3 = FigureCanvasTkAgg(fig3, master=frame)
   canvas_widget3 = canvas3.get_tk_widget()
   canvas_widget3.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


   root.mainloop()

# showGraficos()