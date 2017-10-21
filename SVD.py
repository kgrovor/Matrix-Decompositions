#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:17:26 2017

@author: kshitij
"""
import data
from numpy import linalg as l
import numpy as np
#def svd(M):
    
def get_list(M):
    lmda,eig_vector = l.eig(M)
    lst = []
    for i in range(len(lmda)):
        evect = eig_vector[:,i]
        lst.append([lmda[i],evect])
    
    lst = sorted(lst,key=lambda x: x[0],reverse=True)
    for i in lst:
        i[1] = i[1].real
        i[0] = round(i[0],2)
    return lst
    
    
def svd(M):  
    M = data.M.todense()
    Ulist = get_list(np.dot(M,M.T))
    Vlist = get_list(np.dot(M.T,M))
    U = np.zeros((len(Ulist[0][1]),len(Ulist)))
    V = np.zeros((len(Vlist[0][1]),len(Vlist)))
    
    for i in range(len(Ulist)):
        for j in range(len(Ulist[i][1])):
            U[j][i] = Ulist[i][1][j]
            
    for i in range(len(Vlist)):
        for j in range(len(Vlist[i][1])):
            V[j][i] = Vlist[i][1][j]
    
    V = V.T
    
    sigma = np.zeros((len(Ulist),len(Ulist)))
    for i in range(len(Ulist)):
        sigma[i][i] = Ulist[i][0]**0.5
    return U,sigma,V
        
    

