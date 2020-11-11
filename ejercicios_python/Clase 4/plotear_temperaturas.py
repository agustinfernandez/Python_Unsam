#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:47:31 2020

@author: agustin18
"""


#plotear_temperaturas

import matplotlib.pyplot as plt
import numpy as np

e = np.load('temperaturas.npy')
print(e)

w=plt.hist(e, bins=10)
print(w)
