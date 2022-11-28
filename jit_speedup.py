#!/usr/bin/python3
# Vincent W  @San Jose, CA

from numba import jit
import time
 
def num():
 
    arr = []
    for i in range(100000000):
        arr.append(i)


def make_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    j=0
    for j in range(50000):      # caculate 50000 digits of PI in Python
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2

@jit
def JITmake_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    j=0
    for j in range(50000):      # caculate 50000 digits of PI in Python
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2
 

stime = time.time()
my_array = []

for i in make_pi():
    my_array.append(str(i))


my_array = my_array[:1] + ['.'] + my_array[1:]
big_string = "".join(my_array)
#print ("Here is a big string: %s" % big_string)
etime = time.time() - stime
print('Without optimization.  Calculate 50000 digits of PI in Python spent time :{} seconds'.format(etime))


stime = time.time()
my_array = []

for i in JITmake_pi():
    my_array.append(str(i))

my_array = my_array[:1] + ['.'] + my_array[1:]
big_string = "".join(my_array)
#print ("Here is a big string: %s" % big_string)
etime = time.time() - stime
print('jit optimization.      Calculate 50000 digits of PI in Python spent time :{} seconds'.format(etime))
