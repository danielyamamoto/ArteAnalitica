"""
By: A01658318 - Daniel Yamamoto
*Para poder ejecutar este código es necesario instalar previamente
las librerias de pandas, matplotlib, numpy.
*Además de contar contar con el archivo "covid19_tweets.csv" para
poder obtener los datos que se utilizarán dentro del programa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

covid_data = pd.read_csv("covid19_tweets.csv")
print(covid_data)
print("El tamaño de mis objetos es: ", int(len(covid_data)), "\n")
print(covid_data.describe())

for col in covid_data.columns:
    print(col, ": ", type(col))

x = []
for i in range(len(covid_data)):
    x.append(i)
print(len(x))

plt.subplot(131)
plt.scatter(x, covid_data["user_followers"])
plt.title("USER FOLLOWERS")
plt.xlabel("Data")
plt.ylabel("Quantity")

plt.subplot(132)
plt.scatter(x, covid_data["user_friends"])
plt.title("USER FRIENDS")
plt.xlabel("Data")
plt.ylabel("Quantity")

plt.subplot(133)
plt.scatter(x, covid_data["user_favourites"])
plt.title("USER FAVOURITES")
plt.xlabel("Data")
plt.ylabel("Quantity")

plt.show()