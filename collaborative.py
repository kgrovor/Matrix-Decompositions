#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:48:56 2017

@author: kshitij
"""
# remember to add back mean_array before returning
import data
import numpy as np
from math import sqrt

M = np.array(data.M.todense())

print(M[:,:1])
mean_array = M.mean(0)
sums = {}
for i in range(len(M.T)):
    sums[i] = sqrt(np.sum(M[: , i:i+1]**2))
# Reduce by mean and normalize M column wise
for i in range(len(M[1])):
    for j in range(len(M)):
        if( M[j][i] != 0):
            M[j][i] = (M[j][i] - mean_array[i]) / sums[i]
cosine_sim = M.T * M

#Use formula and return value
row = 3
col = 0





        

