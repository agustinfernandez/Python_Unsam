#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 16:57:08 2020

@author: agustin18
"""


# fileparse.py

import csv

def parse_csv(nombre_archivo):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Lee los encabezados
        headers = next(rows)
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            registro = dict(zip(headers, row))
            registros.append(registro)

    return registros
parse=parse_csv('Data/camion.csv')
print(parse)
# cajones_retenidos = parse_csv('Data/camion.csv', select=['nombre','cajones'])
# print(cajones_retenidos)

#%%


# fileparse.py

def parse_csv(nombre_archivo, select = None):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)
        
        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros

lectura= parse_csv('Data/camion.csv', select = ['nombre', 'cajones'])
print(lectura)

#%%


def parse_csv(nombre_archivo, select = None, types= None):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)
        
        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
        

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros

cajones_lote = parse_csv('Data/camion.csv', select=['nombre', 'cajones'], types=[str, int])
print(cajones_lote)


#%%

###Parse con tuplas

# def parse_csv(nombre_archivo, select = None, types= None,  has_headers=True):
#     '''
#     Parsea un archivo CSV en una lista de registros.
#     Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
#     '''
#     with open(nombre_archivo) as f:
#         filas = csv.reader(f)
#         registros=[]
#         if has_headers==False:
            
            
#             for fila in filas:
#                 if not fila:    # Saltear filas vacías
#                     continue
                
#                 registros.append((fila[0],float(fila[1])))
#             return registros
#         else:
        
#             pass
#         # Lee los encabezados del archivo
#         encabezados = next(filas)
        
#         # Si se indicó un selector de columnas,
#         #    buscar los índices de las columnas especificadas.
#         # Y en ese caso achicar el conjunto de encabezados para diccionarios

#         if select:
#             indices = [encabezados.index(nombre_columna) for nombre_columna in select]
#             encabezados = select
#         else:
#             indices = []
        

#         registros = []
#         for fila in filas:
#             if not fila:    # Saltear filas vacías
#                 continue
#             # Filtrar la fila si se especificaron columnas
#             if indices:
#                 fila = [fila[index] for index in indices]
#             if types:
#                 fila = [func(val) for func, val in zip(types, fila) ]

#             # Armar el diccionario
#             registro = dict(zip(encabezados, fila))
#             registros.append(registro)

#     return registros

# cajones_lote = parse_csv('Data/precios.csv', types=[str,float], has_headers=False)
# print(cajones_lote)

#%%



def parse_csv(nombre_archivo, select = None, types= None,  has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        registros={}
        if has_headers==False:
            
            
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                
                registros[fila[0]]=float(fila[1])
            return registros
        else:
        
            pass
        # Lee los encabezados del archivo
        encabezados = next(filas)
        
        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
        

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros

cajones_lote = parse_csv('Data/precios.csv', types=[str,float], has_headers=False)
print(cajones_lote)

