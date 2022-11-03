# importo librerias

import pandas as pd
import numpy as np

# Ejercicio 1: carga del archivo csv y creacion del primer DataFrame

df_arts = pd.read_csv('datos_arts.csv')

# Ejercicio 2: obtención de un nuevo DataFrame

df_2 = df_arts[['fecha', 'unidades', 'importe']] # tomo las columnas necesarias
df_2 = df_2.groupby(['fecha']).sum() # realizo el agrupamiento por fechas

"""
Ejercicio 3: creación de la variable Sector

creo la lista listacondicion con las condiciones requeridas
creo la lista eleccion con los valores solicitados
Creacion de la variable 'sector' que contendra la logica solicitada
"""
listacondicion = [(df_arts ['grupo'] == '15 LIMPIEZA DEL HOGAR') | (df_arts ['grupo'] == '18 PERFUMERIA'),( df_arts ['grupo'] == '4 LACTEOS') | (df_arts ['grupo'] == '9 FIAMBRERIA')]

eleccion = ['NO COMESTIBLES', 'PERECEDEROS']

df_arts ['sector'] = np.select(listacondicion, eleccion, default= df_arts ['grupo'])

# verifico la condicion restante
df_3=df_arts[((df_arts.sector != "NO COMESTIBLES") & (df_arts.sector != "PERECEDEROS"))]

