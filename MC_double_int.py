# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:01:17 2015
Monte-Carlo Integral approximations
@author: crhea
"""
import numpy as  np
def Double_int_MC(func,a1,b1,a2,b2,n):
    points = np.matrix(np.zeros((n,2)))
    points[:,0] = (np.random.rand(n,1)*(b1-a1)+a1)
    points[:,1] = (np.random.rand(n,1)*(b2-a2)+a2)
    int_val = 0
    for i in range(0,n):    
        int_val += (((b1-a1)*(b2-a2))/n)*func(points[i,0],points[i,1])
    print(int_val)
    
def Triple_int_MC(func,a1,b1,a2,b2,a3,b3,n):
    points = np.matrix(np.zeros((n,3)))
    points[:,0] = (np.random.rand(n,1)*(b1-a1)+a1)
    points[:,1] = (np.random.rand(n,1)*(b2-a2)+a2)
    points[:,2] = (np.random.rand(n,1)*(b3-a3)+a3)
    int_val = 0
    for i in range(0,n):    
        int_val += (((b1-a1)*(b2-a2)*(b3-a3))/n)*func(points[i,0],points[i,1],points[i,2])
    print(int_val)