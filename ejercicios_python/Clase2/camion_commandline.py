#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 02:53:56 2020

@author: agustin18
"""
import csv
import sys


def costo_camion(nombre_archivo):
    
    
    f = open(nombre_archivo, 'rt')
    headers = next(f)
    costo_total=0
    for line in f:
        row = line.split(',')
        suma=float(row[1])*float(row[2])
        costo_total=costo_total+suma
    return costo_total
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'Data/camion.csv'

    
nombre_archivo='Data/camion.csv' 
costo=costo_camion('Data/camion.csv')
print('Costo total:', costo)

    
    