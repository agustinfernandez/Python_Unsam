#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 23:01:25 2020

@author: agustin18
"""
import random

def busqueda_secuencial(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1.
    '''
    pos = -1
    for i,z in enumerate(lista):
        if z == x:
            pos = i
            break
    return pos

busqueda=busqueda_secuencial([0, 3, 5, 6, 9, 12], 6)
print(busqueda)

#%%


def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primer aparición, 
    de lo contrario devuelve -1.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

busqueda2=busqueda_secuencial_([0, 3, 5, 6, 9, 12], 6)
print(busqueda2)

#%%


def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)


m = 10000
n = 100
lista = generar_lista(n, m)
print(lista)



#%%

m = 10000
n = 100
k = 1000
lista = generar_lista(n, m)

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

prom=experimento_secuencial_promedio(lista, m, k)
print(prom)

x = generar_elemento(m)
comps = busqueda_secuencial_(lista, x)[1]
print(comps)

#%%


import matplotlib.pyplot as plt
import numpy as np

m = 10000
k = 1000

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
a=plt.plot(largos,comps_promedio,label = 'Búsqueda Secuencial')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaiciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()

#%%


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
    
m = 10000
n = 100
k = 1000
lista = generar_lista(n, m)

def experimento_binaria_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

prome=experimento_binaria_promedio(lista, m, k)
print(prome)



largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promed = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promed[i] = experimento_binaria_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
b=plt.plot(largos,comps_promed,label = 'Búsqueda Binaria')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaiciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()


#%%
plt.plot(largos,comps_promedio,label = 'Búsqueda Secuencial')
plt.plot(largos,comps_promed,label = 'Búsqueda Binaria')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaiciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()

# Podemos ver en estos gráficos que la búsqueda binaria requiere una cantidad extremadamente menor de comparaciones que la búsqueda secuencial. 
#En este gráfico vemos que la búsqueda binaria es mucho más eficiente que la secuencial. La búsqueda binaria utiliza muchos menos pasos y recursos que la secuencial para llegar a su objetivo.

