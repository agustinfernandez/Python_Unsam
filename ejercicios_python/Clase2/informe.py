#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:18:47 2020

@author: agustin18
"""

from pprint import pprint

def leer_camion(nombre_archivo):
    
    
    f = open(nombre_archivo, 'rt')
    
    headers = next(f)
    camion_lista=[]
    for line in f:
        
        row = line.split(',')
        camion={}
        camion['nombre']=row[0]
        camion['cajones']=int(row[1])
        camion['precio']=float(row[2])
        camion_lista.append(camion)
                             
    return camion_lista
    
    
nombre_archivo='Data/camion.csv' 
camion=leer_camion('Data/camion.csv')
print(camion)



def leer_precios(archivo):
    fd=open(archivo, 'rt')
    headers =next(fd)
    
    precios={}
    for line in fd:
        try:
            row=line.split(',')
            precios[row[0]]=float(row[1])
            print(precios)
           
        except IndexError:
            pass
            
    return precios

precios=leer_precios('Data/precios.csv')
pprint(precios)

#print(precios['Remolacha'])

total=0
for s in camion:
    total += s['cajones']*s['precio']
    
print(total)


cuenta=[]
for x in camion:
    
    try:
    
        if x['nombre'] in precios:
            
            cuenta.append(precios[x['nombre']] * x['cajones'])
            #print(cuenta)
        else:
            print('Dato faltante de' , x['nombre']  )
    except IndexError:
        print('dato faltante')

suma_cuenta=sum(cuenta)
print(suma_cuenta)

ganancia = suma_cuenta-total
print(ganancia)
        
#%%
        
    


def hacer_informe(nombre_archivo1,nombre_archivo2):
	camion = leer_camion(nombre_archivo1)
	precios = leer_precios(nombre_archivo2)
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

#%%


        