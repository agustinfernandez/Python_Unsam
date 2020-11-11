#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 15:48:12 2020

@author: agustin18
"""


# def propagar_al_vecino(l):
#     modif = False
#     n = len (l)
#     for i, e in enumerate(l):
#         if e==1 and i<n-1 and l[i+1] == 0:
#             l[i+1] = 1
#             modif = True
#         if e==1 and i<n-1 and l[i-1] == 0:
#             l[i-1] = 1
#             modif = True
#     return modif

# def propagar(l):
#     m = l.copy()
#     veces = 0
#     while propagar_al_vecino(l):
#         veces += 1
        
#     print(f'Repetí {veces} veces la función propagar_al_vecino.')
#     print (f'Con input {l}')
#     print (f'Y obtuve {m}')
#     return m


# #propagar_al_vecino([0,0,0,0,1])
# propagar([0,0,0,0,1])
# #propagar([0,0,1,0,0])
# #propagar([1,0,0,0,0])

#Respuestas:

# 1) No causan un indexError porque el los if cortan un elemento antes de que la lista llegue a los extremos.
# 2) Porque en propagar([0,0,0,0,1]), tal como está definida la función no se toma en cuenta el último valor de la lista (Con el objetivo de lograr evitar el IndexError, el programa deja de lado un caso importante. El 1 de la última posición debería haberse propagado una vez pero eso no ocurre por eso veces=0). En cambio, en propagar([1,0,0,0,0]) el problema está "invisibilizado" ya que parecería ser que propaga a todas las posiciones (veces=1) .
# 3) Se puede repetir la misma cantidad de veces que el largo de la lista. Hace el largo de la lista-1 operaciones. Esta versión de propagar hace como máximo largodelalista-1 operaciones (cuanto se va hacia la función Propagar_al_vecino) + la correspondiente operación de la función propagar. Es un algoritmo de complejidad cuadrática.

#%%

#Ejercicio 4.4

def propagar_a_derecha(l):
    #print(l)
    n = len(l)
    for i, e in enumerate(l):
        if e==1 and i<n-1:
            if l[i+1]==0:
                l[i+1]=1
    return l
#print(l)    
    
    
def propagar_a_izquierda(l):
    
    return propagar_a_derecha(l[::-1])[::-1]
    

def propagar(l):
    m= l.copy()
    ld=propagar_a_derecha(m)
    lp = propagar_a_izquierda(ld)
    return lp

    

l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
print('Estado original: ', l)
print('Propagando...')
lp=propagar(l)
print('Estado original: ',  l)
print('Estado propagando: ', lp)
    
#
#1) Se modiificó porque Propagar_a_derecha y propagar a la izquierda trabajan sobre la lista L diréctamente, la modifican. Para que eso no pase deberían trabajar sobre una copia de L.
#2) Porque el estado propagado devuelve la lista que realiza las opeciones combinadas de propagar hacia la izquierda y propagar hacia la derecha, LP.
#3)
# def propagar(l):
#     m= l.copy()
#     ld=propagar_a_derecha(m)
#     lp = propagar_a_izquierda(ld)
#     return lp
    
#4) Hace el largo de la lista -1 operaciones.
#5) Como máximo hace propagar_a_derecha=largodelalista-1 + propagar_a_izquierda=largode la lista-1

#%%

#Ejercicio 4.5

def trad2s(l):
    d = {1:'f', 0: 'o', -1: 'x'}
    s=''.join([d[c] for c in l])
    return s

def trad2l(ps):
    inv_d= {'f':1, 'o':0, 'x':-1}
    l = [inv_d[c] for c in ps]
    return l

def propagar(l, debug = True):
    s= trad2s(l)
    if debug:
        print(s)
    W = s.split('x')
    print('a', W)
    PW = [w if ('f' not in w) else 'f'*len(w) for w in W]
    ps= 'x'.join(PW)
    if debug:
        print(ps)
    return trad2l(ps)

l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
lp=propagar(l)
print('Estado original: ', l)
print('Estado propagado: ', lp)
    
#1) Se acorta la lista porque con este comando,  W = s.split('x'), las x que están definidas como -1, son utilizadas como separadores y borradas de la lista.
#2) Sí, se puede de la siguiente forma:
# ps= 'x'.join(PW)

#3) Esta última función es del tipo cuadrática.

