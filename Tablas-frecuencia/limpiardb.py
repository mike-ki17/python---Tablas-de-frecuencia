import pandas as pd
import numpy as np



def melt_DB(archivo_csv):
    df = pd.read_csv(archivo_csv)

    melted_df = pd.melt(df, var_name=None, value_name='Data')
    # melted_df = melted_df['Data']
    tupla_de_datos = tuple(melted_df['Data'])

    data = {}
    df_melt = pd.DataFrame(data)

    df_melt['Data'] = tupla_de_datos

    df_melt.to_csv('datos_limpios.csv', index=False)


    return df_melt


