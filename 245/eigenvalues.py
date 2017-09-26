# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 22:24:53 2015
Carter Rhea
Basic eigenvalues
"""
import numpy as np
A = np.matrix([[3,1,1],[1,8,1],[1,1,4]])
x = np.matrix(np.random.rand(3)).T
n = 3
def euclidean_dist(x,n):
    val = 0
    for i in range(0,n):
        val += x[i,0]**2
    return float(val)**(1/2)
def eigenvalue(A,x,n,ToL):
    err = ToL+1    
    for i in range (1,n):
        U = np.matrix(np.zeros((1,n)))
        U = x/euclidean_dist(x,n)
        x= A*U
        lam = U.T*x
    while err >ToL:
        for i in range (1,n):
            U1 = np.matrix(np.zeros((1,n)))
            U1 = x/euclidean_dist(x,n)
            x1= A*U1
            lam = U1.T*x
        err = abs(euclidean_dist(x1,n)-euclidean_dist(x,n))
        x = x1
    return x,lam

        
    
def main():
    vec , lam =  eigenvalue(A,x,n,10**(-8))
    print("Lambda is %s"%(lam))
main()