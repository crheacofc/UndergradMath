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
            return ['For 0x^2+0x+0 you are just saying 0=0. Hence this is true but boring!']
        else:
            return ["This isn't even true!"]
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
        return imaginary(a,b,c,d)
    if d>=0:
        return real(a,b,c,d)
def main():
    for (x,y,z) in [[2,-10,8],[1,-2,1],[1,0,2],[1,6,25],[0,4,-10],[0,0,0],[0,0,1]]:
        roots = quadsolver(x,y,z)
        if len(roots) == 2:
            print('The roots of %s x^2+ %s x+ %s are %s and %s' %(x,y,z,roots[0],roots[1]))
        else:
            print(roots[0])
main()