#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:10:17 2020

@author: agustin18
"""




def costo_camion(nombre_archivo):
    
    
    f = open(nombre_archivo, 'rt')
    headers = next(f)
    costo_total=0
    for line in f:
        row = line.split(',')
        print(row)
        if (row[1])=='':
            print(f'Falta un dato en la cantidad de cajones de {row[0]} ')
        
        elif(row[2])=='':
            print(f'Falta un dato en el Precio de {row[0]}')
        else:
            
            suma=float(row[1])*float(row[2])
    costo_total=costo_total+suma
    return costo_total
    print(costo_total)
    

costo=costo_camion('Data/missing.csv')
print('Costo total sin tener en cuenta los datos faltantes:', costo)
