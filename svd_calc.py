#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 22:39:28 2017

@author: kshitij
"""

import SVD
import data
import numpy as np
M = data.M.todense()
U, sigma, V = SVD.svd(M)
#left = np.dot(U,sigma)

print M[0]
print "\n"
#print(np.dot(left,M)[0])

abc2 = np.dot(np.dot(U, sigma), V[:943, :])[0]
print abc2
