# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 16:56:44 2016
LU FACTORIZATION AND SUBSEQUENT EQUATION SOLVING
LUalgo
solveUnitLowerTriangular
solveUnitUpperTriangular
errors
LUalgobanded
solveUnitLowerTriangularbanded
solveUnitUpperTriangularbanded


@author: crhea
"""
import numpy as np
def LUalgo(A):
    L = np.matrix(np.zeros((len(A),len(A))))
    U = np.matrix(np.zeros((len(A),len(A))))
    for i in range(0,len(A)):
        L[i,i] = 1
    U[0,:] = A[0,:]
    for k in range(0,len(A)):
        for j in range(k,len(A)):
            add = 0 
            for s in range(0,k):
                add += L[k,s]*U[s,j]
            U[k,j] = A[k,j]-add
        for i in range(k+1,len(A)):
            add = 0 
            for s in range(0,k):
                add += L[i,s]*U[s,k]
            L[i,k] = (A[i,k]-add)/U[k,k]
    return [L,U]
    
def solveUnitLowerTriangular(L,b):
    #c is a column vector as is b
    c = np.matrix(np.zeros((len(L),1)))
    for i in range(0,len(L)):
        add = 0
        for j in range(0,i):
            add += L[i,j]*c[j,0]
        c[i,0] = b[i,0] - add
    return c

def solveUnitUpperTriangular(U,c):
    #x is a column vector as is c
    x = np.matrix(np.zeros((len(U),1)))
    for i in range(len(U)-1,-1,-1):
        add = 0
        for j in range(i+1,len(U)):
            add += U[i,j]*x[j,0]
        x[i,0] = (c[i,0] - add)/U[i,i]
    return x

def errors(A,x_sol,b,x):
    #x_sol est ce que tu as reçu de solveUnitUpperTriangular
    r = A*x_sol-b
    back_abs = abs(r).max()
    back_rel = back_abs/abs(b).max()
    err_abs = abs(x-x_sol).max()
    err_rel = err_abs/abs(x).max()
    
    return [r,back_abs,back_rel,err_abs,err_rel]

##pour un banded matrix
def LUalgobanded(A,p):
    L = np.matrix(np.zeros((len(A),len(A))))
    U = np.matrix(np.zeros((len(A),len(A))))
    for i in range(0,len(A)):
        L[i,i] = 1
    U[0,:] = A[0,:]
    for k in range(0,len(A)):
        for j in range(k,len(A)):
            add = 0 
            for s in range(k-p,k):
                add += L[k,s]*U[s,j]
            U[k,j] = A[k,j]-add
        for i in range(k+1,len(A)):
            add = 0 
            for s in range(k-p,k):
                add += L[i,s]*U[s,k]
            L[i,k] = (A[i,k]-add)/U[k,k]
    return [L,U]
    

def solveUnitLowerTriangularbanded(L,b,p):
    #c is a column vector as is b
    c = np.matrix(np.zeros((len(L),1)))
    for i in range(0,len(L)):
        add = 0
        for j in range(0,i):
            add += L[i,j]*c[j,0]
        c[i,0] = b[i,0] - add
    return c

def solveUnitUpperTriangularbanded(U,c,p):
    #x is a column vector as is c
    x = np.matrix(np.zeros((len(U),1)))
    for i in range(len(U)-1,-1,-1):
        add = 0
        for j in range(i-(p+1),len(U)):
            add += U[i,j]*x[j,0]
        x[i,0] = (c[i,0] - add)/U[i,i]
    return x
'''
Ab = np.matrix([[2,6,0,0,0],[2,3,3,0,0],[0,3,5,3,0],[0,0,6,1,2],[0,0,0,2,3]])
xb = np.matrix([5,2.2,5,2,3]).T
bb = np.dot(Ab,xb)

L, U = LUalgobanded(Ab,1)
Ln,Un = LUalgo(Ab)
#print("%s \n %s"%(L,U))
c_sol = solveUnitLowerTriangularbanded(L,bb,1)
x_sol = solveUnitUpperTriangularbanded(U,c_sol,1)
#print(x_sol)
'''