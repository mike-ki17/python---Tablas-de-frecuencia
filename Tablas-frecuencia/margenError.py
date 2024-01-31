import pandas as pd
import numpy as np

# db_tabla_frecuecia_agrupada = './tabla_frecuencias_agrupado_regla_Sturges.csv' # -0.2
# db_tabla_frecuecia_agrupada = './tabla_frecuencias_agrupado_3.csv'  # -0.4
# db_tabla_frecuecia_agrupada = './tabla_frecuencias_agrupado_2.csv'  # -0.13
# db_tabla_frecuecia_agrupada = './tabla_frecuencias_agrupado_regla_Sturges_2.csv' # 0.2

def ErrorRelativo ():
        
    db_tabla_frecuencia = './tabla_frecuencias.csv'
    db_tabla_frecuecia_agrupada = './tabla_frecuencias_agrupado.csv'  # -0.13

    df0 = pd.read_csv(db_tabla_frecuencia)
    df1 = pd.read_csv(db_tabla_frecuecia_agrupada)

    total_xf = np.sum(df0['X*F'])
    total_xf_a = np.sum(df1['X*F'])

    margenError = round(((total_xf / total_xf_a) * 100) - 100, 2)
    # print(total_xf, total_xf_a,  margenError)
    return margenError