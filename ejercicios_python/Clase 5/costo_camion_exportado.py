#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:57:25 2020

@author: agustin18
"""


#import costo_camion
from informe_funciones import leer_camion

# costo_camion.costo_camion('Data/camion.csv')
# print(costo_camion)



def costo_camion(nombre_archivo):
    
    camion=leer_camion(nombre_archivo)
    print(camion)
    costo_total=0
    for line in camion:
            suma=(line['cajones'])*(line['precio'])
    costo_total=costo_total+suma
    return costo_total
    print(costo_total)
    

costo=costo_camion('Data/camion.csv')
print('Costo total sin tener en cuenta los datos faltantes:', costo)
