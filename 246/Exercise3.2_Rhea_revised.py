# -*- coding: utf-8 -*-
"""
Carter Rhea <crhea@g.cofc.edu>
Spetember 17, 2015
This program will print out the first "n" fibonacci numbers that you i
"""
n = eval(input('Enter a natural number n, greater than or equal to 0: '))
if n < 0 or (n != int(n)) :
    print("Warning: that's not a natural number!")
else:
    if n==0:
        print('The fibonacci number is 0')
    elif n==1:
        print('The fibonacci number is 1')
    else:
        lis =[]
        lis.append(0)
        lis.append(1)
        for i in range(2,n):
            f_n= lis[i-1] +lis[i-2]
            lis.append(f_n)
        print('Our fibonacci numbers are',lis)
        