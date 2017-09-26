# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:26:17 2015

@author: crhea
"""
import numpy as np
def cramers(A,b): 
##This program will use Cramer's rule to determine x values given a
##Matrix A and another b where Ax=b. type cramers(A,b).
    [m,n]=A.shape;
    if m != n:
        print('MUST BE SQUARE!!!') 
    
    else:
        D = np.linalg.det(A);
        for k in range(1,n):
            A_0 = A;
            A_0[:,k] = b;
            E = np.linalg.det(A_0);
            x_k = E/D;
            return x_k

        