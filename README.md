<h1 align="center">	🍊Examen naranjas🍊</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/Examen_naranjas)

***
<h2>¿De qué trata esta tarea?</h2>

En esta tarea se nos pide crear un dataset sobre naranjas, el cual luego debemos analizar y calcular su media, mediana, moda, desviación tipica y cuartiles. Asimismo encontramos una parte visual proporcionada por tres distintas gráficas: barras, sectores y dispersion.

***

<h2>Código:</h2>

```
import pandas as pd #utilizamos pandas para crear un dataframe con los datos de las naranjas
import numpy as np #es una biblioteca que utilizamos para funciones matemáticas
import matplotlib.pyplot as plt #utilizamos matplotlib para crear un gráfico
import seaborn as sns #utilizamos seaborn para crear un gráfico


def Naranjas():
    df= pd.DataFrame(np.random.randint(100, 230, 100), columns=['naranjas'])
    df = df.dropna() #eliminamos los valores nulos con dropna
    df.sort_values(by=['naranjas'], inplace=True)
    df.to_csv('naranjas.csv', index= False)
    df= pd.read_csv('naranjas.csv')
    return df
print(Naranjas())



def media(df):
    media = df['naranjas'].mean() #con ayuda de pandas calculamos la media utilizando la función mean
    return media
print('La media es:', media(Naranjas()))



def desviacion(df):
    desviacion = df['naranjas'].std()
    return desviacion
print('La desviación típica es:', desviacion(Naranjas()))



def mediana(df):
    mediana = df['naranjas'].median()
    return mediana
print('La mediana es:', mediana(Naranjas()))




def moda(df):
    moda = df['naranjas'].mode()
    return moda
print('La moda es:', moda(Naranjas()))



def cuartiles(df):
    cuartil1 = df['naranjas'].quantile(0.25)
    cuartil2 = df['naranjas'].quantile(0.5)
    cuartil3 = df['naranjas'].quantile(0.75)
    return cuartil1, cuartil2, cuartil3
print('Los cuartiles son:', cuartiles(Naranjas()))




def menos_130(df):
    menos_130 = df['naranjas'][df['naranjas'] < 130].count()
    return menos_130
print(f'Hay {menos_130(Naranjas())} naranjas que pensan menos de 130')



def sectores_naranjas(df):
    fig, ax = plt.subplots()
    sectores = ['<130', '130', '>130']
    porcentajes = [df['naranjas'][df['naranjas'] < 130].count()/df['naranjas'].count()]
    porcentajes.append(df['naranjas'][(df['naranjas'] == 130)].count()/df['naranjas'].count())
    porcentajes.append(df['naranjas'][(df['naranjas'] > 130)].count()/df['naranjas'].count())
    ax.pie(porcentajes, labels=sectores, autopct='%1.1f%%', startangle=90)
    plt.title('Diagrama sectores:', color= 'white')
    plt.show()
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

```
***

<h2>Explicación paso a paso del código:</h2>

**Pasos:**

**1.** En primer lugar importamos las librerías que necesitamos para desarrollar el programa, en esta ocasión hemos importado las siguientes librerias:

       -Pandas: Esta librería la utilizamos para leer y crear el Dataframe.
       -Numpy: Esta librería nos proporciona una gran cantidad de funciones matemáticas, de las cuales usamos por ejemplo: .mean(), .std(), .mean()...
       -Matplotlib.pyplot: Esta librería lo que nos permite es la creación de gráficos en dos dimensiones, como diagrama de barras, histogramas...
       -Seaborn: Esta libreria se podría explicar como una extensión del Matplotlib.
 
 **2.** A continuación creamos uba función donde se crea el dataset, el cual es limpiado; eliminando los valores nulos con uso de la función **dropna** y ordenado con ayuda de la función conocida como **sort**. Asimismo dentro de esta función encontramos su lectura con uso de **Pandas**.
 
 **3.** Ahora creamos distintas funciones con las que haremos los calculos estadísticos, dentro de cada función usamos la librería numpy para realizar los cálculos.
 
        -media: para su cálculo utilizamos la función .mean()
        -desviación típica: para su cálculo utilizamos la función .std()
        -mediana: para su cáculo utilizamos la función .median()
        -moda: para su cálculo utilizamos la función .mode()
        -cuartiles: para su cálculo utilizamos la función .quantile()

**4.** Creamos una funcion que nos muestre la cantidad de naranjas que pensan menos de 130 gramos. Para que cuente la cantidad utilizamos la función .count()

**5.** Por último creamos los distintos diagramas.
       
       -Diagrama de sectores: utilizamos la librería Matplotlib. Dentro de esta función encontramos uso de diversas funciones como son:
       
                              *ax.pie(): se utiliza para trazar gráficos circulares.
                              *plt.subplots(): es una función que devuelve una tupla que contiene una figura y objeto (s) de ejes. Por lo tanto, al usar fig, ax = plt.subplots() descomprime esta tupla en las variables fig y ax. Teniendo fig es útil si desea cambiar los atributos a nivel de figura o guardar la figura como un archivo de imagen más tarde (por ejemplo, con fig.savefig('yourfilename.png')).
                              *plt.title(): lo utlizamos para especificar el título de la visualización representada.
    
       -Diagrma de barras: utilizamos dos librerías: Matplotlib y Seaborn.
                           
                              *sns.countplot(): se usa para mostrar los conteos de observaciones en cada contenedor categórico usando barras.
                             
       
       -Diagrama de dispersión: utilizamos la libreía Matplotlib.
       
                               *plt.scatter(): se usa para crear diagramas de dispersión

***
       
 <h2>Explicación diagramas:</h2>
