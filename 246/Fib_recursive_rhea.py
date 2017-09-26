# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:53:29 2015

@author: crhea
"""
def Fib(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)

def main():
    n = eval(input("How many iterations would you like?  "))
    for k in range(n):
        num = Fib(k)
        print("The fibonacci number is %s at iteration %s"%(num,k+1))

main()