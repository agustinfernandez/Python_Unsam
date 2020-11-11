#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:33:15 2020

@author: agustin18
"""


#busqueda_en_listas.py

def busqueda_lineal_ordenada(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    lista_ordenada=sorted(lista)
    print(lista_ordenada)
    pos = -1  # comenzamos suponiendo que e no está
    i = 0     
    for z in lista_ordenada:  # recorremos los elementos de la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
        i += 1       
    return pos

busqueda=busqueda_lineal_ordenada([1, 4, 54, 3, 0, -1, 2], 3)
print(busqueda)



#para el caso de listas ordenadas, de forma que la función pare cuando encuentre un elemento mayor a e