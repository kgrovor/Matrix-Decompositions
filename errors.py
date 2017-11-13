#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:26:38 2017

@author: bhavathi
"""
from sklearn.metrics import mean_squared_error
from math import sqrt
import scipy as sp
import numpy as np
import test

def calc_error(M):
    M_test=test.M.todense();
    print(M_test.shape)
    print(M.shape)
    #rms = sqrt(mean_squared_error(M_test[np.nonzero(M_test)], M[np.nonzero(M_test)]))
    #spm=sp.stats.spearmanr(M_test[np.nonzero[M_test]], M[np.nonzero[M_test]])
    print (rms)
    print(spm)
    return 0