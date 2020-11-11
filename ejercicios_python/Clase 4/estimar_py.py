#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 20:43:46 2020

@author: agustin18
"""


def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

N=100000
M=0
for i in range(N):
    x, y= generar_punto()
    if x**2 + y**2 < 1:
        M+=1
print(f' pi - {4*M/N}')


