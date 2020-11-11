#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:10:17 2020

@author: agustin18
"""


f = open('Data/camion.csv', 'rt')
headers = next(f)
headers
costo_total=0
for line in f:
    row = line.split(',')
    suma=float(row[1])*float(row[2])
    costo_total=costo_total+suma
print(costo_total)

    
    