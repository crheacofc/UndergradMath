# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 21:18:35 2016
For my final Project for Math 445
This creates the grid for the Galerkin Finite Element method (K) and the function and boundary vectors
Main func:
Stiff - creates the stiff matrix given: n_elements,s_elements. and K
F - functional values for the right hand side of the equation
LUalgobanded - From Project1_module
solveUnitLowerTriangularbanded - From Project1_module
solveUnitUpperTriangularbanded - From Project1_module

Parameters:
start - begining position of elements
end - end position of elements
n_elements - number of nodes
s_elements - number of S functions
S_i - transformation function left hand side
S_j - transformation function right hand side
K - finite element equation for stiff matrix
q - q(x) function - needed for the computation of K
f - function initially on right hand side of ODE before Weak Form
@author: crhea
"""
import numpy as np
import scipy as sp

def Stiff(K,S_i,S_j,q,n_elements,s_elements,start,end):
    ## Take a look at the end points to make sure we are getting everything.
    ## Maybe start a bit earlier
    h = (end-start)/n_elements
    J = h/2
    Stiff_matrix = np.zeros((n_elements,n_elements))
    for k in range(0,n_elements-1):
        for i in range(k,k+s_elements):
            dS_i = sp.misc.derivative(S_i,i) #derivative of S_i
            x_i = start+k*h
            for j in range(k,k+s_elements):
                dS_j = sp.misc.derivative(S_j,j) #derivative of S_j
                if i==j:
                    Stiff_matrix[i,j] += sp.integrate.quad(lambda x: K(S_i(x),S_i(x),dS_i,dS_i,q,J,x_i),-1,1)[0]
                else: 
                    Stiff_matrix[i,j] += sp.integrate.quad(lambda x: K(S_i(x),S_j(x),dS_i,dS_j,q,J,x_i),-1,1)[0]
    Stiff_matrix[0,0] *= 2.
    Stiff_matrix[-1,-1] *= 2.
    return Stiff_matrix
    
def F(f,S_i,S_j,n_elements,s_elements,start,end):
    h = (end-start)/n_elements
    J = h/2
    F = np.zeros(n_elements)
    for k in range(n_elements-1):
        x_i = start+k*h
        x_j = x_i+h
        F[k] += sp.integrate.quad(lambda x:f(((x_j-x_i)/2)*x+(x_i+x_j)/2)*S_i(x)*J,-1,1)[0]
        F[k+1] += sp.integrate.quad(lambda x:f(((x_j-x_i)/2)*x+(x_i+x_j)/2)*S_j(x)*J,-1,1)[0]
    F[0] *= 2.
    F[-1] *= 2.
    return F

def LUalgobanded(A,p):
    L = np.zeros((len(A),len(A)))
    U = np.zeros((len(A),len(A)))
    for i in range(len(A)):
        L[i,i] = 1
    U[0,:] = A[0,:]
    for k in range(len(A)):
        for j in range(k,len(A)):
            add = 0
            for s in range(k-p,k):
                add += np.dot(L[k,s],U[s,j])
            U[k,j] = A[k,j]-add
        for i in range(k+1,len(A)):
            add = 0
            for s in range(k-p,k):
                add += np.dot(L[i,s],U[s,k])
            L[i,k] = (A[i,k]-add)/U[k,k]
    return [L,U]


def solveUnitLowerTriangularbanded(L,b,p):
    #c is a column vector as is b
    c = np.zeros(len(L))
    for i in range(len(L)):
        add = 0
        for j in range(i):
            add += np.dot(L[i,j],c[j])
        c[i] = b[i] - add
    return c

def solveUnitUpperTriangularbanded(U,c,p):
    #x is a column vector as is c
    x = np.zeros(len(U))
    for i in range(len(U)-1,-1,-1):
        add = 0
        for j in range(i-(p+1),len(U)):
            add += np.dot(U[i,j],x[j])
        x[i] = (c[i] - add)/U[i,i]
    return x
    
    
