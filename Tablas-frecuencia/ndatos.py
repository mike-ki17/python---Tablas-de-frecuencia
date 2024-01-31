import pandas as pd
import numpy as np
import sys
import csv

# Obtener el nombre del archivo CSV como argumento
if len(sys.argv) != 2:
    print("Uso: python3 ndatos.py archivo.csv")
    sys.exit(1)

archivo_csv = sys.argv[1]

# Leer y procesar la base de datos
try:
    with open(archivo_csv, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        # Realizar el análisis de datos aquí
        # for row in reader:
        #     # Procesar cada fila de datos según tus necesidades
        #     print(row)
    # print(archivo_csv)
except FileNotFoundError:
    print(f"No se encontró el archivo: {archivo_csv}")
except Exception as e:
    print(f"Ocurrió un error al procesar el archivo: {str(e)}")


# bd = './csv/bd_estadistica.csv'
bd = archivo_csv
df = pd.read_csv(bd)
column1Df = df.iloc[:, 0]


def medidas_TC (D) :

    media = round(D.mean(), 2)
    mediana = round(D.median(), 2)
    frecuencia_acomulada = D.sum()

    frecuencias = {}
    for i in D:
        count = 0

        for a in D:
            if i == a:
                count += 1
        frecuencias[i]=count

    valor_max = max(frecuencias.values())

    for clave, valor in frecuencias.items():
        if valor == valor_max:
            clave_maxima = clave
            break
    moda = clave_maxima

    frecuencia_p = frecuencias.items()
    frecuencia_p = sorted(frecuencia_p)
    x,f = zip(*frecuencia_p)

    return [media, mediana, moda, frecuencia_acomulada, frecuencias, x, f]

mtc = medidas_TC(column1Df)


def medidas_D (mtc):

    n = len(df)
    h_porcentaje = []
    dispercion_m = []
    dispercion_s = []
    varianza = []
    fi_values = []
    hi_values = []
    xporf_values = [] 
    frecuencia_abs = 0    
    sumatoria_h = 0

    for clave, valor in mtc[4].items():
        h = round((valor / n)*100, 2) 
        h_porcentaje.append(h)

        x_media = round(clave - mtc[0], 2)
        dispercion_m.append(abs(x_media))

    for i in dispercion_m:
        dispercion_s.append(abs(i))

    # for i in dispercion_s:
    #     dispercion_m.append(abs(i))
    
    for i in dispercion_m:
        x_m_cuadrado = round(i**2, 4)
        varianza.append(x_m_cuadrado)
   
    for i in mtc[6]:
        frecuencia_abs = frecuencia_abs + i
        fi_values.append(frecuencia_abs)
   
    for i in h_porcentaje:
        sumatoria_h = round(sumatoria_h + i, 2)
        hi_values.append(sumatoria_h)


    for i in range(len(mtc[5])):
        xporf_values.append(mtc[5][i] * mtc[6][i])



    return [n, h_porcentaje, dispercion_m, dispercion_s, varianza, frecuencia_abs,fi_values, hi_values, xporf_values]


mdd = medidas_D(mtc)

def tabla (mtc, mdd):

    data = {}
    df2 = pd.DataFrame(data)

    x_values = mtc[5]
    f_values = mtc[6]

    df2['X'] = x_values
    df2['F'] = f_values
    df2['H%'] = mdd[1]
    df2['Fi'] = mdd[6]
    df2['Hi'] = mdd[7]
    df2['X*F'] = mdd[8]
    df2['X-M'] = mdd[2]
    df2['|X-M|'] = mdd[3]
    df2['X-M²'] = mdd[4]


    df2.to_csv('tabla_frecuencias.csv', index=False)

tabla(mtc,mdd)