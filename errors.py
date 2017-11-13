#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:26:38 2017

@author: bhavathi
"""
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np
import scipy as sp
import test

def calc_error(M):
    M_test=test.M.todense()
    M=M[:M_test.shape[0],:M_test.shape[1]]
    rms = sqrt(mean_squared_error((M_test[np.nonzero(M_test)]).T, M[np.nonzero(M_test)]))
    spm=sp.stats.spearmanr(M_test[np.nonzero(M_test)].T, M[np.nonzero(M_test)])
    print (rms)
    print(spm)
    return 0