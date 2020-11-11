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



def primer_tirada(n):
    tirada=[]
    x= tirar(n)
    #print(x)
    for i in range(0,len(x)-1):  
        
        for z in range (i+1, len(x)):
          
            if x[i]==x[z] and len(tirada)==0:
            
                tirada.append(x[i])
                tirada.append(x[z])
            elif x[i]==x[z]:
               
                tirada.append(x[i])
                
        if len(tirada)>0:
            break
    
    return tirada
primera=primer_tirada(5)
#print(primera)            
            
def segunda_tirada(n, tirado):
    
    if len(tirado)==0:
        jugar=primer_tirada(n)
        return jugar
        
    w=tirar(n-len(tirado))
    #print(w)
    
    for i in range(0, len(w)):
        
        if w[i]==tirado[0] and len(tirado)>0:
            tirado.append(w[i])
    return tirado


segunda=segunda_tirada(5, primera)
#print(segunda)
    
def tercer_tirada(n, tiradas_ant):
    if len(tiradas_ant)==0:
        jugar_otra=primer_tirada(n)
        return jugar_otra

    s=tirar(n-len(segunda))
    #print(s)
    
    for i in range(0, len(s)):
        if s[i]==tiradas_ant[0] and len(tiradas_ant)>0:
            tiradas_ant.append(s[i])
    return tiradas_ant

terceraa=tercer_tirada(5, segunda)
#print(terceraa)
            
    
def generala_noservida(partida):

    if len(partida)==5:
        resultado=1
    else:
        resultado=0
    
    return resultado
    
resulta=generala_noservida(terceraa)
#print(resulta)

def generalaa(l):
    prueba=[]
    for i in range(0, l):
        
        ld=primer_tirada(5)
    
        lp=segunda_tirada(5, ld)
        lz=tercer_tirada(5, lp)
        G=generala_noservida(lz)
        prueba.append(G)
        
    
    return prueba
N=10000
general=generalaa(N)
#print(general)

promedio= N/ sum(general)
print(promedio)






