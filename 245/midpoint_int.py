##This program will use the midpoint rule of approximate integration to approximate the value of an integral!
#Func is the function you wish to evaluate, a is the start, b is the end, n is the number of steps!
n=1000
a=0.
b=10.
delta_x=(b-a)/float(n)
func = (val+2)
x = numpy.linspace((a+delta_x)/2,(b-delta_x)/2,n-1)
s = 0
for val in x:
    y = lambda val: func
    if val == (a+delta_x)/2:
        s = y(val)
    else:
        s = s+y(val)
sums = s*delta_x
sums
