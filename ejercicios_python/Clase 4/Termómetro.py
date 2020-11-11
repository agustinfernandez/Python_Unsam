#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 21:56:54 2020

@author: agustin18
"""
import numpy as np
import random
#termometro.py

# for i in range(6):
#         print(f'{random.normalvariate(0,1):.2f}', end=', ')
        
        
def termometro(n):
    resultados=[]
    for i in range (n):
        resultados.append(random.normalvariate(37.5,0.2))
    return resultados

resultado_termometro=termometro(999)
print(resultado_termometro)

#el valor máximo: 
print(max(resultado_termometro))
#el mínimo:
print(min(resultado_termometro))
#el promedio
print(np.mean(resultado_termometro))
#la mediana:
print(np.median(resultado_termometro))

a = np.array(resultado_termometro)
print(a)

np.save('temperaturas', a)
