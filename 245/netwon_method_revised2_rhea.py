# -*- coding: utf-8 -*-
"""
Carter Rhea <crhea@g.cofc.edu>
September 28, 2015
Iterate until error of zero
"""


from math import sin,cos
f=lambda x: 10-2*x+sin(x)
f_prime=lambda x: -2+cos(x)
def newton(f,f_prime,x_0,ToL): 
    x_n1=x_0
    x_n = x_n1-f(x_n1)/f_prime(x_n1)
    err= abs(x_n-x_n1)
    k=0
    val=[]
    while (err>0):
        x_n=x_n1-f(x_n1)/f_prime(x_n1)
        err = abs(x_n-x_n1)
        x_n1=x_n
        k+=1
        val.append([x_n,err,k])
    return val

def main():
    for j in [10**(-8),0]:
        vals = newton(f, f_prime, 3., j)
        for val in vals:
            print('The root is %s with an error of %s with %s function evaluations' %(val[0],val[1],2*val[2]))
main()