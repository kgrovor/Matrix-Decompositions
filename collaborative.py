#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:48:56 2017

@author: kshitij
"""
# remember to add back mean_array before returning
import data
import numpy as np

M = np.array(data.M.todense())

print(M[:,:1])
mean_array = M.mean(0)

# Handling Strict and generous raters
for i in range(len(M)):
    for j in range(len(M[i])):
        if( M[i][j] != 0 ):
            M[i][j] = M[i][j] - mean_array[j]


sim = {}
for i in range(len(M[1])):
    summed = 0
    if (i,i+1) not in sim:
        for j in range(len(M)):
            summed = summed + M[j][i] * M[j][i+1] 


#Use formula and return value
row = 3
col = 0





        

