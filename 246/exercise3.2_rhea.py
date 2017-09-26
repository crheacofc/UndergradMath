# -*- coding: utf-8 -*-
"""
Exercise 3.2 
Carter Rhea <crhea@g.cofc.edu>



"""

#This program will take a natural number then compute and print the first n Fibonacci numbers.
n = eval(input('Enter a natural number n, greater than or equal to 0: '))
if n < 0 or (n != int(n)) :
    print("Warning: that's not a natural number!")
else:
    if n==0:
        print('The fibonacci number is 0')
    elif n==1:
        print('The fibonacci number is 1')
    else:
        lis =[0,1]
        f_n2=lis[0]
        f_n1=lis[1]
        for i in range(0,n-2):
            f_n= f_n1+f_n2
            lis.append(f_n)
            f_n2 = f_n1
            f_n1 = f_n
        print(lis)
        