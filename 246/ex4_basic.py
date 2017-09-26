# -*- coding: utf-8 -*-
"""
Carter Rhea <crhea@g.cofc.edu>
September 17, 2015
This will solve quadratics and then print out the roots!!!!!!
"""

from math import sqrt
## now we solve for roots that are real and imaginary...
def imaginary(a,b,c,d):
     real = -b/(2*a)
     imaginary = sqrt(abs(d))/(2*a)
     root0 = real+imaginary*1j
     root1 = real-imaginary*1j
     return [root0,root1]

def real(a,b,c,d):
    if (a==0 and b==0):
        if c ==0:
            print('0=0')
            return 0
        else:
            print('This isnt even true!')
            return 0
    elif a !=0:
        if d > 0:
            root0 = (-b + sqrt(b**2 - 4 * a * c))/(2 * a)
            root1 = (-b - sqrt(b**2 - 4 * a * c))/(2 * a)
            return [root0,root1]
        elif d == 0:
            root0 = -b/(2*a)
            return[root0,'since the discriminant equals 0 there is only 1 root']
    elif a==0:
        root0 = -c/b
        return [root0,'the equation is linear and only has 1 root!']
    elif a==0 and c==0 and b!=0:
        root0==0
        return[0,'the only root is 0']
    
def quadsolver(a,b,c):
    d = b**2-4*a*c
    if d <0:
        roots =  imaginary(a,b,c,d)
    if d>=0:
        roots = real(a,b,c,d)
    print('The roots of',a,'x^2+',b,'x+',c,'are',roots[0], 'and', roots[1])
for i in [[2,-10,8],[1,-2,1],[1,0,2],[1,6,25],[0,4,-10]]:
    quadsolver(i[0],i[1],i[2])