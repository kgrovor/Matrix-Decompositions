#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import data
import numpy as np
from math import sqrt

M = np.array(data.M.todense())


mean_array = M.mean(1)
sums = {}

# Reduce by mean and normalize M column wise
for i in range(len(M[1])):
    for j in range(len(M)):
        if( M[j][i] != 0):
            M[j][i] = (M[j][i] - mean_array[j]) 
for i in range(len(M.T)):
    sums[i] = sqrt(np.sum(M[: , i:i+1]**2))
for i in range(len(M[1])):
    for j in range(len(M)):
        if( M[j][i] != 0):
            M[j][i] = (M[j][i]) / sums[i] 

cosine_sim = np.dot(M.T, M)

def find_nearest(user,movie):
    arr = cosine_sim[user]
    near = []
    arr = np.abs(arr-arr[movie])
    arr = np.delete(arr,movie)
    for i in range(850):
        temp = arr.argmin()
        near.append(temp)
        arr = np.delete(arr,temp) 
    return near
    
    
    
def collab_rating(user,movie):
    tops = find_nearest(user,movie)
    count = 0
    tot = 0
    flag = 1
    denominator = 0
    for i in tops:
        if M[user][i] > 0:
            count = count + 1
            if count > 41:
                break
            tot = tot + np.abs(cosine_sim[movie][i]) * (M[user][i] * sums[i])
            denominator = np.abs(cosine_sim[movie][i]) + denominator
            flag = 0
    if(flag == 1):
        denominator = 1
    tot = tot/denominator
    return (tot + mean_array[user]) 


        

