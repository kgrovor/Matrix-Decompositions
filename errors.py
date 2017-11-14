#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:26:38 2017

@author: bhavathi
"""
import numpy as np
import test

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

def spear(predictions, targets):
    return np.mean(1-(6*np.sum(np.square(predictions - targets),axis=1)/predictions.shape[1]/((predictions.shape[1])**2 - 1)))

def calc_error(M):
    M_test=np.matrix(test.M.todense())
    M=np.matrix(M[:M_test.shape[0],:M_test.shape[1]])
    actual=np.squeeze(np.asarray(M_test[np.nonzero(M_test)]))
    predicted=np.squeeze(np.asarray(M[np.nonzero(M_test)]))

    rms=rmse(predicted, actual)
    M[M_test==0]=0
    Pred=np.argsort(-M)
    Act=np.argsort(-M_test)

    spm=spear(Act,Pred)
    print ("RMSE : ", rms)
#    print(spear(predicted,actual))
    print("Spearman Correlation Coefficient : ",spm*100)
    
    k=100
    precision=0.0
    Pred=Pred[:,:k]
    Act=Act[:,:k]
    for i in range(Pred.shape[0]):
        for j in Pred[i,:]:
            if (j in Act[i,:]):
                precision=precision+1
                
    precision=precision/Pred.shape[0]
    print("Precision on top ",k," : ",precision*100,"%")
    return 0
