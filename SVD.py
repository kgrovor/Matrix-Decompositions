#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of SVD with and without retained energy
"""
from numpy import linalg as l
import numpy as np

#def svd(M):

def get_list(M_symmetric):
    """
    Takes input of M*M.T form of a square matrix. Calculates eigenvector-eigenvalue pairs and returns them as a list of pairs sorted with respect to the eigenvalue in a descending order
    """
    lmda, eig_vector = l.eig(M_symmetric)
    lst = []
    for i in range(len(lmda)):
        evect = eig_vector[:, i]
        lst.append([lmda[i], evect])
    lst = sorted(lst, key=lambda x: x[0], reverse=True)
    for i in lst:
        #i[1] = i[1].real
        i[1] = np.real(i[1])
        #if i[1][0] < 0:
            #i[1][0] = i[1][0]* -1
            #i[1][0] = 999
        i[0] = round(i[0], 2)

    return lst

def svd(M):
    """
    Singular value decomposition of M
    """

    Ulist = get_list(np.dot(M, M.T))
    Vlist = get_list(np.dot(M.T, M))
    U = np.zeros((len(Ulist[0][1]), len(Ulist)))
    V = np.zeros((len(Vlist[0][1]), len(Vlist)))
    i = None

    for i in range(len(Ulist)):
        for j in range(len(Ulist[i][1])):
            U[j][i] = Ulist[i][1][j]

    for i in range(len(Vlist)):
        for j in range(len(Vlist[i][1])):
            V[j][i] = Vlist[i][1][j]

    V = V.T

    sigma = np.zeros((len(Ulist), len(Vlist)))

    for i in range(len(Ulist)):
        sigma[i][i] = Ulist[i][0]**0.5

    for i in range(len(sigma)):
        temp = np.dot(M,np.matrix(V[i]).T)
        temp_U = np.matrix(U[:,i]).T
        flag = False
        for j in range(len(temp)):
            if temp_U[j] !=0.0:
                if temp[j]/temp_U[j] <0.0 :
                    flag=True
                    break  
        if flag :
            for k in range(len(U[:,i])):
                U[k][i]=-1*U[k][i]

    return U, sigma, V

def svd_retained_energy(M,e):
    """
    Argument e decides the amount of energy to be retained. i.e .9 for 90%
    """
    mean=np.squeeze(np.asarray(np.true_divide(M.sum(1),(M!=0).sum(1))))
    
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if M[i,j]!=0:
                M[i,j]=M[i,j]-mean[i]
    U, sigma, V = svd(M)
        
    if (e<1):
        
        diag = np.sum(np.diagonal(sigma)**2)
        energy = e*(diag)
        singulars = np.diagonal(sigma)
        i = None
        for i in range(len(singulars)-1, 0, -1):
            if(diag - singulars[i]**2 < energy):
                break
            else:
                diag = diag - singulars[i]**2
    
    
        sigma = sigma[0:i+1, 0:i+1]
        U = U[::, 0:i+1]
        V = V[0:i+1, ::]
    #print(diag)
    #print(np.sum(np.diagonal(U)))
    
    
    Y=l.multi_dot([U,sigma,V])
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
                Y[i,j]=Y[i,j]+mean[i]
    return U, sigma, V, Y

def svd_for_cur(M,e):
    """
    Implementation of SVD for use in the CUR function. 
    """
    U, sigma, V = svd(M)
        
    if (e<1):
        
        diag = np.sum(np.diagonal(sigma)**2)
        energy = e*(diag)
        singulars = np.diagonal(sigma)
        i = None
        for i in range(len(singulars)-1, 0, -1):
            if(diag - singulars[i]**2 < energy):
                break
            else:
                diag = diag - singulars[i]**2
    
    
        sigma = sigma[0:i+1, 0:i+1]
        U = U[::, 0:i+1]
        V = V[0:i+1, ::]

    return U, sigma, V
    
#U, V, S, Y= svd_retained_energy(data.M.todense(),1)
#errors.calc_error(Y)
#U, V, S, Y= svd_retained_energy(data.M.todense(),0.9)
#errors.calc_error(Y)
