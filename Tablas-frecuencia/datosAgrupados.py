import pandas as pd
import numpy as np
import sys
import csv

# Obtener el nombre del archivo CSV como argumento
if len(sys.argv) != 3:
    print("Uso: python3 datosAgrupados.py archivo.csv K")
    sys.exit(1)

archivo_csv = sys.argv[1]
Kintervalos = sys.argv[2]


# Leer y procesar la base de datos
try:
    with open(archivo_csv, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        
except FileNotFoundError:
    print(f"No se encontró el archivo: {archivo_csv}")
except Exception as e:
    print(f"Ocurrió un error al procesar el archivo: {str(e)}")


# db = './csv/tabla_frecuencias.csv'
db = archivo_csv
db_origin = './csv/bd_estadistica.csv'
bdNA = './tabla_frecuencias.csv'

df = pd.read_csv(db)
dfO = pd.read_csv(db_origin)


#===== Variables =====

max = max(df['X'])
min = min(df['X'])

R = max - min
# K = round(np.floor(1 + 3.322 * np.log(len(df['X']))))
K = int(Kintervalos)
rango = (1, 100)
A = np.floor(R / K)




def try_intervalos(mgerr):

    clat = [(round(min - mgerr), round((min + A) - mgerr))]
    xi = min + A

    for i in range(K-1):
        xi = (xi + 1 + A)
        clat.append((round((xi - A) - mgerr), round(xi - mgerr)))
    
    return clat


cla = [(round(min), round(min + A))]
x = min + A
for i in range(K-1):
    x = x + 1 + A
    cla.append((round(x - A), round(x)))
    if round(x) > rango[1]:
        mgerr = round(x - rango[1])
        cla = try_intervalos(mgerr)


def media_intervalos (I) :
    x_values = []
    for i in range(len(I)):
        x_values.append(round(np.mean(I[i])))

    return x_values


mk = media_intervalos(cla)
media = round(np.mean(mk))


def frecuencia (I):

    intervalosSec0 = []
    intervalosSec1 = []
    # print(I[0][0],  I[0][1])
    for i in I:
        intervalosSec0.append(i[0])
        intervalosSec1.append(i[1])


    frecuencias = []
   
    def fValues (a, b):
        sumNum = 0
        for i in df['X']:
            if i >= a and i <= b:
                fila_columna_encontrada = df.loc[df['X'] == i, ['F']].sum().sum()
                sumNum += fila_columna_encontrada
        frecuencias.append(sumNum)


    for i in range(K):
        fValues(intervalosSec0[i], intervalosSec1[i])
    
    return frecuencias


f_values = frecuencia(cla)
n = np.sum(f_values)

def frecuancia_absoluta_acomulada (frecuencias):
    frecAbs = 0
    f_acomulada = []
    for i in frecuencias:
        frecAbs = frecAbs + i
        f_acomulada.append(frecAbs)
    
    return f_acomulada


f_abs = frecuancia_absoluta_acomulada(f_values)


def frecuencia_relativa_H (F):
    frec_relativa = []
    n_datos = np.sum(F)
    for i in F:
        fr = round((i / n_datos) * 100, 3)
        frec_relativa.append(fr)

    porcentaTotaljeFrecuenciaRElativa = np.sum(frec_relativa)

    return frec_relativa

h_values = frecuencia_relativa_H(f_values)

def frecuencia_relativa_acomulada_H(h_values):
    frec_relativa_acom = []
    sumatoria_h = 0

    for i in h_values:
        sumatoria_h = round(sumatoria_h + i, 3)
        frec_relativa_acom.append(sumatoria_h)

    return frec_relativa_acom
    

hi_values = frecuencia_relativa_acomulada_H(h_values)

def x_valuesporf_values (x_values, f_values):

    xv_fx = []
    for i in range(len(x_values)):
        # print(x_values[i], f_values[i], (x_values[i] * f_values[i]) )
        xv_fx.append(round(x_values[i] * f_values[i]))

    return xv_fx

xporf = x_valuesporf_values(mk, f_values)
xmedia = round((np.sum(xporf)) / n, 2)


# ====== Disperción =====

def dispercionS (mk, xmedia):
    # xmedia = sum(x*f) / n

    # print(xmedia)
    xMenosMedia = []
    xMenosMediaAbs = []
    xMenosMediaCua = []

    for i in range(len(mk)):
        xMenosMedia.append(round(mk[i] - xmedia, 4))

    for i in xMenosMedia:
        xMenosMediaAbs.append(round(abs(i)))
        xMenosMediaCua.append(round(i**2))



    return [xMenosMedia, xMenosMediaAbs, xMenosMediaCua]

disperción_S_values = dispercionS(mk, xmedia)



def tabla (cla, mk, f_values, f_abs, h_values, hi_values, xporf, disperción_S_values):
    data = {}
    dfAgrupado = pd.DataFrame(data)

    dfAgrupado['Clases'] = cla
    dfAgrupado['X'] = mk
    dfAgrupado['F'] = f_values
    dfAgrupado['H%'] = h_values
    dfAgrupado['Fi'] = f_abs
    dfAgrupado['Hi'] = hi_values
    dfAgrupado['X*F'] = xporf
    dfAgrupado['X-M'] = disperción_S_values[0]
    dfAgrupado['|X-M|'] = disperción_S_values[1]
    dfAgrupado['X-M²'] = disperción_S_values[2]


    dfAgrupado.to_csv('tabla_frecuencias_agrupado.csv', index=False) #sep='\t'


tabla(cla, mk, f_values, f_abs, h_values, hi_values, xporf, disperción_S_values)
