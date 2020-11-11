#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 15:01:30 2020

@author: agustin18
"""
import numpy as np
import random
import matplotlib.pyplot as plt


def crear_album(figus_total):
    vacio=[]
    i=0
    while i<figus_total:
        vacio.append(0)
        i=i+1
    return vacio

album_vacio=crear_album(6)
#print(album_vacio)

def album_incompleto(A):
    i=0
    a=False
    while i<len(A):
        if A[i]==0:
            a=True
        i+=1
    return a

incompleto=album_incompleto(album_vacio)
#print(incompleto)

def comprar_figu(figus_total):
    figu=random.randint(0,figus_total-1)
    return figu
comprar=comprar_figu(6)
#print(comprar)
    
def cuantas_figus(figus_total):
    nuevo=crear_album(figus_total)
    
    count=0
    i=0
    while album_incompleto(nuevo)  == True:
        compra=comprar_figu(figus_total)
        
        if nuevo[compra]==0:
            nuevo[compra]=1
        else:
            nuevo[compra]=nuevo[compra]
        
        i+=1
        count+=1
    return count
cuantas=cuantas_figus(6)
#print(cuantas)

# def repeticiones(n,figus_total):
#     resultados=[]
#     i=0
#     while i<n:
#         r=cuantas_figus(figus_total)
#         resultados.append(r)
        
#         i=i+1
#     promedio= np.mean(resultados)
#     return resultados, f'el promedio estimado para {n} casos con {figus_total} figuritas es {promedio}'

# rep=repeticiones(100,670)
# #print(rep)
    
def comprar_paquete(figus_total, figus_paquete):
    paquete=[]
    i=0
    while i < figus_paquete:
        azaar=random.randint(0, figus_total-1)
        
        paquete.append(azaar)
        i+=1
    return paquete
paquetillo=comprar_paquete(10,5)
print(paquetillo)


    
def cuantos_paquetes(figus_total, figus_paquete):
    nuevo=crear_album(figus_total)
    
    count=0
    i=0
    while album_incompleto(nuevo)  == True:
        compra=comprar_paquete(figus_total,figus_paquete)
        z=0
        while z<len(compra): 
            
            if nuevo[compra[z]]==0:
                nuevo[compra[z]]=1
            else:
                nuevo[compra[z]]=nuevo[compra[z]]
            z+=1
        
        i+=1
        count+=1
        
    return count
cuantas_paquetes=cuantos_paquetes(670,5)
print(cuantas_paquetes)

def repeticiones(n,figus_total,figus_paquete):
    
    resultados=[]
    i=0
    while i<n:
        r=cuantos_paquetes(figus_total,figus_paquete)
        resultados.append(r)
        
        i=i+1
    promedio= np.mean(resultados)
    return resultados, promedio
N=100
rep=repeticiones(N,670,5)
print(rep)
    
def prob(lista):
    resul=[]
    for i in range(len(lista)):
        if lista[i]<=850:
            resul.append(lista[i])
    print(resul)
    o= len(resul)/N
    return o

probb=prob(rep)
print(probb)

plt.hist(rep,bins=10)

#Para completar el albumal 90% debemos reemplazar en repeticiones a figus_total, por el valor del 90% del álbum. Es decir 603 en cambio de 670. El resultado es de 860 paquetes.

# Para calcular sin figus repetidas en paquete:

    
# def comprar_paquete(figus_total, figus_paquete):
#     paquete=[]
#     i=0
#     while i < figus_paquete:
#         azaar=random.randint(0, figus_total-1)
#         if azaar not in paquete:
#             paquete.append(azaar)
#             i=i+1
#         else:
#             i=i
#     return paquete
# paquetillo=comprar_paquete(10,5)
# print(paquetillo)




