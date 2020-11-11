#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:29:18 2020

@author: agustin18
"""


def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    comps = 0
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        comps += 1
        medio = (izq + der) // 2
        
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medbusqueda_binaria([1, 3, 5], 0, verbose = True)io] < x:
            izq = medio + 1 # descarto mitad izquierda
        
    return pos, comps

a=busqueda_binaria([1, 3, 5, 7, 9], 7, verbose = True)
print(a)

# Si usamos  medio = (izq + der) / 2 la variable repsuesta sería de punto flotante. Esto nos arrojaría el siguiente error de formato:"Unknown format code 'd' for object of type 'float'".

#%%


def donde_insertar(lista, x, verbose = False):
   
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    
    der = len(lista) -1
    
    while izq <= der:
        medio = (izq + der) // 2
       
        
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            
            pos = f'{lista[medio]} se encuentra en la posición {lista.index(lista[medio])}.'     # elemento encontrado!
            return pos
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista  < x:
            izq = medio + 1 # descarto mitad izquierda
        
        
    pos=f'{x} no se encuentra en la lista pero podría insertarse en la posición {lista.index(lista[izq])}.'     
            
    return pos

a=donde_insertar([1, 3, 5, 6, 9, 22, 44, 50], 50 , verbose = True)
print(a)

#%%

#5.12

def insertar(lista, x, verbose = False):
   
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    
    der = len(lista) -1
    
    while izq <= der:
        medio = (izq + der) // 2
       
        
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            
            pos = f'{lista[medio]} se encuentra en la posición {lista.index(lista[medio])}.'     # elemento encontrado!
            return pos
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista  < x:
            izq = medio + 1 # descarto mitad izquierda
        
    lista.insert(lista.index(lista[izq]), x)
    
    pos= f'{x} lo inserto en la lista en la posición {lista.index(lista[izq])}.'     
            
    return lista, pos

a=insertar([1, 3, 5, 6, 9, 22, 44, 50], 45 , verbose = True)
print(a)

    
    
    
