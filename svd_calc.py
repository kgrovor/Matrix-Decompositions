#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 22:39:28 2017

@author: kshitij
"""

import SVD
import data
from numpy import linalg as l
import numpy as np
M = data.M.todense()
print(M)
mean=np.squeeze(np.asarray(np.true_divide(M.sum(1),(M!=0).sum(1))))

for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        if M[i,j]!=0:
            M[i,j]=M[i,j]-mean[i]
print(M)
print(sum(M.T))

U, sigma, V = SVD.svd(M)
#left = np.dot(U,sigma)

s,v,d = l.svd(M)



print("\n")
print(U[0,:20])
print("\n")       
print(s[0,:20])

#print(U)
print("\n")
#print(np.dot(left,M)[0])

#abc2 = np.dot(np.dot(U, sigma), V[:943, :])[0]
#print(abc2)
