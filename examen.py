#haz un dataframe con una funcion que tenga una variable llamada naranjas y tenga 100 lineas con valores entre 100 y 230
#limpia el dataframe
#ordena los datos de menor a mayor y lo guardas en un csv
#abre el archivo csv y guardalo en un dataframe
#imprime el dataframe


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def Naranjas():
    naranjas = np.random.randint(100, 230, 100)
    df = pd.DataFrame(naranjas, columns=['naranjas'])
    df.dropna(inplace=True)
    df.sort_values(by='naranjas', inplace=True)
    df.to_csv('naranjas.csv')
    df= pd.read_csv('naranjas.csv')
    return df
print(Naranjas())
