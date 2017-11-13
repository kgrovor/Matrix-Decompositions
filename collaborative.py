#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import data
import numpy as np
import errors

M = np.array(data.M.todense())

M_norm= np.zeros((M.shape[0], M.shape[1]))
mean_array=np.squeeze(np.asarray(np.true_divide(M.sum(1),(M!=0).sum(1))))

# Reduce by mean and normalize M column wise
for i in range(M.shape[1]):
    for j in range(M.shape[0]):
        if( M[j,i] != 0):
            M_norm[j,i] = (M[j,i] - mean_array[j]) 


def user_user_collab():
    sum_u=np.sqrt(np.squeeze(np.asarray(np.sum(np.square(M),axis=1))))
    M_u=(M_norm.T/sum_u).T
    user_sim = np.dot(M_u,M_u.T)
    user_sim[user_sim < 0] = 0

    collab_user = np.zeros((M.shape[0], M.shape[1]))
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            collab_user[i,j]=np.dot(user_sim[i], M[:,j])/np.sum(user_sim[i])

    return collab_user            

    
def item_item_collab():
    sum_i=np.sqrt(np.squeeze(np.asarray(np.sum(np.square(M),axis=0))))
    M_i=(M_norm/sum_i)
    item_sim = np.dot(M_i.T, M_i)
    item_sim[item_sim < 0] = 0
    
    collab_item = np.zeros((M.shape[0], M.shape[1]))
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            collab_item[i,j]=np.dot(item_sim[j], M[i,:])/np.sum(item_sim[j])

    return collab_item

    
def user_user_base():
    sum_u=np.sqrt(np.squeeze(np.asarray(np.sum(np.square(M),axis=1))))
    M_u=(M_norm.T/sum_u).T
    user_sim = np.dot(M_u,M_u.T)
    user_sim[user_sim < 0] = 0

    mean_u=np.squeeze(np.asarray(np.true_divide(M.sum(1),(M!=0).sum(1))))
    mean_i=np.squeeze(np.asarray(np.true_divide(M.T.sum(1),(M.T!=0).sum(1))))
    mean_m=np.mean( M[np.nonzero(M)] )
    base = np.zeros((M.shape[0], M.shape[1]));
    base=((base+mean_m+mean_i).T+mean_u).T
    M_base=M-base
    
    base_user = np.zeros((M.shape[0], M.shape[1]))
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            base_user[i,j]=np.dot(user_sim[i], M_base[:,j])/np.sum(user_sim[i])
    base_user=base_user+base
    
    return base_user
    
def item_item_base():
    sum_i=np.sqrt(np.squeeze(np.asarray(np.sum(np.square(M),axis=0))))
    M_i=(M_norm/sum_i)
    item_sim = np.dot(M_i.T, M_i)
    item_sim[item_sim < 0] = 0
    
    mean_u=np.squeeze(np.asarray(np.true_divide(M.sum(1),(M!=0).sum(1))))
    mean_i=np.squeeze(np.asarray(np.true_divide(M.T.sum(1),(M.T!=0).sum(1))))
    mean_m=np.mean( M[np.nonzero(M)] )
    base = np.zeros((M.shape[0], M.shape[1]));
    base=((base+mean_m+mean_i).T+mean_u).T
    M_base=M-base
    
    base_item = np.zeros((M.shape[0], M.shape[1]))
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            base_item[i,j]=np.dot(item_sim[j], M_base[i,:])/np.sum(item_sim[j])
    base_item=base_item+base

    return base_item
   
    
#
errors.calc_error(user_user_collab())
errors.calc_error(item_item_collab())
errors.calc_error(user_user_base())
errors.calc_error(item_item_base())


#def find_nearest(user,movie):
#    arr = user_sim[user]
#    near = []
#    arr = np.abs(arr-arr[movie])
#    arr = np.delete(arr,movie)
#    for i in range(850):
#        temp = arr.argmin()
#        near.append(temp)
#        arr = np.delete(arr,temp) 
#    return near
#    
#    
#    
#def collab_rating(user,movie):
#    tops = find_nearest(user,movie)
#    count = 0
#    tot = 0
#    flag = 1
#    denominator = 0
#    for i in tops:
#        if M[user][i] > 0:
#            count = count + 1
#            if count > 41:
#                break
#            tot = tot + np.abs(cosine_sim[movie][i]) * (M[user][i] * sums[i])
#            denominator = np.abs(cosine_sim[movie][i]) + denominator
#            flag = 0
#    if(flag == 1):
#        denominator = 1
#    tot = tot/denominator
#    return (tot + mean_array[user]) 


        

