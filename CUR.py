#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 21:20:23 2017

@author: bhavathi
"""
import SVD
from numpy import linalg as l
import data
import numpy as np

def cur(M):
    """
    CUR decomposition of M
    """
    
    r= 10
    M = data.M.todense()
    print(M.shape)
    temp = np.squeeze(np.asarray(np.sum(np.square(M))))
    
    col_prob=temp/float(sum(temp))
    temp = np.squeeze(np.asarray(np.sum(np.square(M),axis=1)))
    row_prob=temp/float(sum(temp))
    rows = np.random.choice( len(row_prob), r,replace=False, p=row_prob)    
    cols = np.random.choice( len(col_prob), r, replace=False , p=col_prob)  

    C=M[rows,:] 
    R=M[:,cols]
    W=M[rows[:, None], cols]

    S, V, D = SVD.svd(W)
    product=[D.T, l.matrix_power(l.pinv(V),2), S.T]
    print(D.T.shape)
    print(l.matrix_power(l.pinv(V),2).shape)
    print(S.T.shape)
    U=l.multi_dot(product)
        
    return C,U,R
    
C,U,R=cur(data.M.todense())
print(C)
print("\n")
print("\n")
print(U)
print("\n")
print("\n")
print(R)
print("\n")
