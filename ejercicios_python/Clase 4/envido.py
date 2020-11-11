#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 16:10:06 2020

@author: agustin18
"""
import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

azaar=random.sample(naipes,k=3)
#print(azaar)

def envido(n):
    resultados=[]
    jugada=random.sample(naipes,k=n)
    #print(jugada)
    previo=[]
    
    if jugada[0][1] == jugada[1][1] and jugada[0][0]<=7 and jugada[1][0]<=7:
        
        previo.append(jugada[0][0]+jugada[1][0])
    
    elif jugada[0][1] == jugada[2][1] and jugada[0][0]<=7 and jugada[2][0]<=7:
        
        previo.append(jugada[0][0]+jugada[2][0])
        
        
    elif jugada[1][1] == jugada[2][1] and jugada[1][0]<=7 and jugada[2][0]<=7:
        
        previo.append(jugada[1][0]+jugada[2][0])
        
    elif jugada[0][1] == jugada[1][1] and jugada[0][0]>=10 and jugada[1][0]<=7 and len(previo)==0:
        
        previo.append(jugada[1][0])
        
    elif jugada[0][1] == jugada[1][1] and jugada[1][0]>=10 and jugada[0][0]<=7 and len(previo)==0:
        
        previo.append(jugada[0][0])
        
    elif jugada[0][1] == jugada[2][1] and jugada[0][0]>=10 and jugada[2][0]<=7 and len(previo)==0:
        
        previo.append(jugada[2][0])
        
    elif jugada[0][1] == jugada[2][1] and jugada[2][0]>=10 and jugada[0][0]<=7 and len(previo)==0:
        
        previo.append(jugada[0][0])
        
    elif jugada[1][1] == jugada[2][1] and jugada[1][0]>=10 and jugada[2][0]<=7 and len(previo)==0:
        
        previo.append(jugada[2][0])
        
    elif jugada[1][1] == jugada[2][1] and jugada[2][0]>=10 and jugada[1][0]<=7 and len(previo)==0:
        
        previo.append(jugada[1][0])
        
    if len(previo)==0:
        resultados.append(0)
    else:
        resultados.append(max(previo)+20)
    
    return resultados

resul=envido(3)
        
#print(resul)
        
def probabilidades(n, jugadas):
    res=[]
    for i in range(0, jugadas):
        a=envido(3)
        
        if a[0]==n:
            res.append(a[0])
    print(res)
    return res.count(n)


NUM=100000
prop=probabilidades(33,NUM)
print(prop)

probabilidades_de_envido= prop/NUM
print(probabilidades_de_envido)
#31=0.02854
#32= 0.01435
#33= 0.01371
            
            
        
        