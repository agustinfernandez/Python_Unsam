#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:29:35 2020

@author: agustin18
"""


import random


dado = random.randint(1, 6)
#print(dado)

#%%

import random

tirada = []

for i in range (5):
    tirada.append(random.randint(1,6))
    
#print(tirada)


#%%False

#Generala Servida



def tirar(n):
    tirada=[]
    for i in range(n):
        tirada.append(random.randint(1, 6))
        #print(tirada)
    return tirada
        
n=5
tirado=tirar(n)
#print(tirado)

# def es_generala(tiradas):
#     #print(tiradas)
#     for i in range(0, len(tiradas)-1):
#         b = False
#         if tiradas[0] == tiradas[i+1]:
#             b = True
#     return b

# a=es_generala(tirado)

# #print(a)   
# N=1000000
# G = sum(es_generala(tirar(5)) for i in range (N))
# prob = G/N


print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la propabolidad de sacar generala servida mediante {prob:.6f}.')

#1) Porque al haber más número de intentos, el promedio que se saca es más estable.
#2) Podríamos decir que sale entre 0.16 y 0.17 generalas promedio.
#3) En realidad no creo que podamos decir una probabilidad de forma exacta, porque si es exacta dejaría de ser probabilidad. Aún así, para acercarnos más al valor más certero, podría calcular una buena cantidad de promedio y hacer el promedio entre ellos..

#%%






