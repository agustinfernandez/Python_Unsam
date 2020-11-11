#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 23:35:19 2020

@author: agustin18
"""

import csv
import os
import matplotlib.pyplot as plt
import numpy as np

f = open('Data/arbolado-en-espacios-verdes.csv')
rows = csv.reader(f)
headers = next(rows)
headers

row=next(rows)
indices = [headers.index(nombre) for nombre in headers]
indices

arboleda= [{nombre:row[dato] for nombre,dato in zip(headers, indices)} for row in rows ]
#print(arboleda)

H=[float(arbol['altura_tot']) for arbol in arboleda]
print(H)

G=[float(arbol['diametro']) for arbol in arboleda]
print(G)

jacaranda_alt = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
#print(len(jacaranda))

jacaranda_dim = [float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']

jacaranda2 = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
#print(jacaranda2)

os.path.join('Data', 'arbolado-en-espacios-verdes.csv')

altos = [float(arbol['altura_tot']) for arbol in arboleda]
plt.hist(altos,bins=10)

plt.scatter(jacaranda_dim, jacaranda_alt, s=10, color='red', alpha=0.2)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")

# Considero que en el gŕafico podemos ver que a medida que si el diámentro del jacarandá es mayor, también lo es su altura. Podemos ver una relación lineal entre estas dos variables.
 