#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:26:38 2017

@author: bhavathi
"""
import numpy as np
from scipy.stats import spearmanr as spearm
import test

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

def spear(predictions, targets):
    return 1-(6*np.sum((predictions - targets) ** 2)/len(predictions)/(len(predictions)**2 - 1))

def calc_error(M):
    M_test=np.matrix(test.M.todense())
    M=np.matrix(M[:M_test.shape[0],:M_test.shape[1]])
    actual=np.squeeze(np.asarray(M_test[np.nonzero(M_test)]))
    predicted=np.squeeze(np.asarray(M[np.nonzero(M_test)]))

    rms=rmse(predicted, actual)
    spm=spearm(actual,predicted)
    print ("RMSE : ", rms)
#    print(spear(predicted,actual))
    print("Spearman Result :\n\t","Correlation : ",spm[0],"\n\tResult : ",spm[1])
    
    M[M_test==0]=0
    k=10
    precision=0.0
    Pred=np.argsort(M)[:,:k]
    Act=np.argsort(M_test)[:,:k]

    for i in range(Pred.shape[0]):
        for j in Pred[i,:]:
            if (j in Act[i]):
                precision=precision+3
                
    precision=precision/k/Pred.shape[0]
    print("Precision on top ",k," : ",precision*100,"%")
    return 0

#calc_error (data.M.todense())