from cgitb import html
import pandas as pd

#cargar los datos en python
dataframe = pd.read_csv('.\empleados.csv')
#print(dataframe)   # este print imprime como un consolidado

# cargar todos los datos

#print(dataframe.to_string()) # este print imprime todos los datos

#cargar los primro n registro de una banco de datos
#print(dataframe.head())  # con estos imprime los primero 5
#print(dataframe.head(20)) # con esto imprimo los primeros 5

# cargar los ultimos n registro de un banco de datos
#print(dataframe.tail()) # este trae los ultimos 5 de la BD
#print(dataframe.tail(20))# con esto imprimo los primeros 5
# obtener informacion de los datos cargados
#print(dataframe.info())## trae informacion de lo que tiene la BD, campos. datos vacios, tamaño BD, tipo de dato
#print(dataframe.describe())

#acceder a datos o registros especificos
#print(dataframe["nombres"].head)
#print(dataframe["salario"].tail(20))


# acceder a registro por su indice

#print(dataframe.iloc[20:30]) # CON ESTE MUESTRA LOS DATOS POR INDICE DESDE EL 20 HASTA EL 30

#print(dataframe.loc[[10,20,30,40]]) ## ingresamos a los registros especificos de esas filas ojo siempre doble corchete

# deseo consultar los registros pero solo al nombre y al salario

#print(dataframe.loc[[1,5,10],['nombres', 'salario']]) # con este imprimio lo anterior

# pero lo vamos a crearlo en una variable que se llame HTML
#estoy exportando una tabla
'''
tabla=(dataframe.loc[[1,5,10],['nombres', 'salario']])

html = tabla.to_html()
text_file=open('index.html','w')
text_file.write(html)
text_file.close()

'''

#FILTROS CON CONDICIONES LOGICAS

#print(dataframe[dataframe['salario']>5500000]).head(10)

print(dataframe[(dataframe['salario']>5500000)&(dataframe['cargo']=='analista2')])
