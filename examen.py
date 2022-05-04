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
    df= pd.DataFrame(np.random.randint(100, 230, 100), columns=['naranjas'])
    df = df.dropna()
    df.sort_values(by=['naranjas'], inplace=True)
    df.to_csv('naranjas.csv', index= False)
    df= pd.read_csv('naranjas.csv')
    return df
print(Naranjas())

#haz una función que haga la media de los datos


def media(df):
    media = df['naranjas'].mean()
    return media
print('La media es:', media(Naranjas()))

#haz una función que haga la desviación típica de los datos


def desviacion(df):
    desviacion = df['naranjas'].std()
    return desviacion
print('La desviación típica es:', desviacion(Naranjas()))

#haz una función que haga la mediana de los datos


def mediana(df):
    mediana = df['naranjas'].median()
    return mediana
print('La mediana es:', mediana(Naranjas()))

#haz una función que haga la moda de los datos


def moda(df):
    moda = df['naranjas'].mode()
    return moda
print('La moda es:', moda(Naranjas()))

#haz una funcion que calcule los cuartiles de los datos
#el cuartil 1 es el 25%
#el cuartil 2 es el 50%
#el cuartil 3 es el 75%


def cuartiles(df):
    cuartil1 = df['naranjas'].quantile(0.25)
    cuartil2 = df['naranjas'].quantile(0.5)
    cuartil3 = df['naranjas'].quantile(0.75)
    return cuartil1, cuartil2, cuartil3
print('Los cuartiles son:', cuartiles(Naranjas()))

#haz una función que te diga cuantas naranjas pensan menos de 130


def menos_130(df):
    menos_130 = df['naranjas'][df['naranjas'] < 130].count()
    return menos_130
print(f'Hay {menos_130(Naranjas())} naranjas que pensan menos de 130')


def sectores_naranjas(df): #nos muestra un diagrama de sectores divididos en tres sectores
    #Función que dibuja un diagrama de sectores con los porcentajes de naranjas de cada sector
    #Definimos a figura y los ejes del gráfico
    fig, ax = plt.subplots()
    #Definimos los sectores
    sectores = ['<130', '130', '>130']
    #Definimos los porcentajes de naranjas de cada sector
    porcentajes = [df['naranjas'][df['naranjas'] < 130].count()/df['naranjas'].count()]
    porcentajes.append(df['naranjas'][(df['naranjas'] == 130)].count()/df['naranjas'].count())
    porcentajes.append(df['naranjas'][(df['naranjas'] > 130)].count()/df['naranjas'].count())
    #Dibujamos el diagrama de sectores
    ax.pie(porcentajes, labels=sectores, autopct='%1.1f%%', startangle=90)
    plt.title('Diagrama sectores:', color= 'white')
    #Mostramos el gráfico
    plt.show()
    #guardamos el gráfico en la carpeta graficos_img
    fig.savefig('graficos_img/sectores_naranjas.png')
print(sectores_naranjas(Naranjas()))

def barras_naranjas(df):
    plt.figure(figsize=(10,5))
    sns.countplot(df['naranjas'])
    plt.title('Diagrama de barras:', color= 'black')
    plt.xlabel('Peso')
    plt.ylabel('Naranjas')
    plt.xticks(rotation=90, fontsize=8)
    plt.savefig('graficos_img/barras_naranjas.png')  
    plt.show()
    plt.close()
print(barras_naranjas(Naranjas()))

#crea una funcion que muestre una grafica de dispersión de los datos


def dispersión(df):
    df= pd.read_csv('naranjas.csv')
    data=df['naranjas'].groupby(pd.cut(df['naranjas'], range(100,240,10))).count()
    fig, ax = plt.subplots()
    lista = []
    for i in range(100,230,10):
        lista.append(i)
    plt.scatter(lista,data)
    plt.title('Diagrama de dispersión:', color= 'black')         
    plt.show()
    fig.savefig('graficos_img/dispersion_naranjas.png')
print(dispersión(Naranjas()))









