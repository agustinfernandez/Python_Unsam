#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:52:28 2020

@author: agustin18
"""

#Ejercicio 5.8

from fileparse import parse_csv

def hacer_informe(nombre_archivo1,nombre_archivo2):
	camion = parse_csv('Data/camion.csv',select=['nombre','cajones','precio'], types=[str,int,float])
	precios = parse_csv('Data/precios.csv',types=[str,float], has_headers=False)
	headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
	sep = ('----------')
	print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
	print(f'{sep:>10s} {sep:>10s} {sep:>10s} {sep:>10s}')
	lista = []
	for s in camion:
		lista = ((s['nombre'],s['cajones'],'$'+str(s['precio']),precios[s['nombre']]-s['precio']))
		print('%10s %10d %10s %10.2f' % lista)
    


informe=hacer_informe('Data/fecha_camion.csv','Data/precios.csv')
print(informe)

