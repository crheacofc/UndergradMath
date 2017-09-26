# -*- coding: utf-8 -*-
"""
Carter Rhea <crhea@g.cofc.edu>
September 17, 2015
"""

#This program will take a natural number then compute and print all fibonacci numbers less than or equal to n
n = eval(input('Enter a natural number n, greater than or equal to 0: '))
if n < 0 or (n != int(n)) :
    print("Warning: that's not a natural number!")
else:
    if (n==0):
        print("Fibonacci number is 0")
    elif (n==1):
        print("Fibonacci number is 1")
    else:
        lis =[0,1]
        f_n= lis[0]+lis[1]
        i=2
        while (f_n <= n):
            f_n= lis[i-2]+lis[i-1]
            i+= 1
            if (f_n <= n):
                lis.append(f_n)
        print(lis)
  