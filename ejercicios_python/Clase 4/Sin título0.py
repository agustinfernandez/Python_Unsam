#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 10:10:07 2020

@author: agustin18
"""


# def tienen_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i<n:
#         if expresion[i] == 'a':
#             return True
#         else:
#            return False
#         i+=1


# rta = tienen_a('palabra')
# print(rta)
#%%


#Ejercicio 4.1: Debugger
#
# def invertir_lista(lista):
#     invertida=[]
#     i=len(lista)
#     while i>0:
#         i= i-1
#         invertida.append (lista.pop(i))
#     return invertida

# l= [1, 2, 3, 4, 5]
# m= invertir_lista(l)

# print(f'Entrada{l}, Salida: {m}')

#El primer paso clave en donde se modifica el parámetro de entrada es en "invertida.append(lista.pop(i))", ya que el lista.pop borra el último elemento de la lista.

#%%

#Ejercicio 4.2:

import csv 
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezado= next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion=leer_camion('Data/camion.csv')
pprint(camion)

#Sobre escriba todos los registro{} con los datos de la fila que entran al for.


    
    