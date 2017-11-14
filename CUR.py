#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 21:20:23 2017

@author: bhavathi
"""
import SVD
from numpy import linalg as l
import numpy as np


def cur_without_repeat(M,e):
    """
    CUR decomposition of M
    """
    
    r= 50
    mean_val=np.squeeze(np.asarray(np.true_divide(M.sum(1),(M!=0).sum(1))))
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if M[i,j]!=0:
                M[i,j]=M[i,j]-mean_val[i]

    temp = np.squeeze(np.asarray(np.sum(np.square(M),axis=0))) 
    col_prob=temp/float(sum(temp))

    temp = np.squeeze(np.asarray(np.sum(np.square(M),axis=1)))
    row_prob=temp/float(sum(temp))
    rows = np.random.choice( len(row_prob), r,replace=False, p=row_prob)    
    cols = np.random.choice( len(col_prob), r, replace=False , p=col_prob)  

    R=(M[rows,:].T/np.sqrt(r*row_prob[rows])).T
    C=M[:,cols]/np.sqrt(r*col_prob[cols])
    W=M[rows[:, None], cols]
    S, V, D = SVD.svd_for_cur(W,0.9)
    
    product=[D.T, l.matrix_power(l.pinv(V),2), S.T]
    U=l.multi_dot(product)
    Y=l.multi_dot([C,U,R])

    Y=(Y.T+mean_val).T

    return C,U,R,Y 

def cur_with_repeat(M,e):
    """
    CUR decomposition of M
    """
    
    r= 50
    mean_val=np.squeeze(np.asarray(np.true_divide(M.sum(1),(M!=0).sum(1))))
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if M[i,j]!=0:
                M[i,j]=M[i,j]-mean_val[i]

    temp = np.squeeze(np.asarray(np.sum(np.square(M),axis=0))) 
    col_prob=temp/float(sum(temp))

    temp = np.squeeze(np.asarray(np.sum(np.square(M),axis=1)))
    row_prob=temp/float(sum(temp))
    rows = np.random.choice( len(row_prob), r,replace=True, p=row_prob)    
    cols = np.random.choice( len(col_prob), r, replace=True , p=col_prob)  

    R=(M[rows,:].T/np.sqrt(r*row_prob[rows])).T
    C=M[:,cols]/np.sqrt(r*col_prob[cols])
    W=M[rows[:, None], cols]
    S, V, D = SVD.svd_for_cur(W,0.9)
    
    product=[D.T, l.matrix_power(l.pinv(V),2), S.T]
    U=l.multi_dot(product)
    Y=l.multi_dot([C,U,R])

    Y=(Y.T+mean_val).T

    return C,U,R,Y 

#C,U,R,Y=cur(data.M.todense(),0.9)
#
#errors.calc_error(Y)

#print(C)
#print("\n")
#print("\n")
#print(U)
#print("\n")
#print("\n")
#print(R)
#print("\n")

