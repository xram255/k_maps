import numpy as np
from time import sleep as delay

r = np.array([[0, 0, 0, 0],
              [0, 0, 0, 0],
              [1, 1, 1, 0],
              [0, 1, 0, 0]])

c = r.T

#--Scan All--
'''
inc1 = 0
inc2 = 0
for indx1 in r:
    inc1 += 1
    for indx2 in indx1:
        inc2 += 1
        if(indx2 == 1):
            print(inc1, inc2)
    inc2 = 0
        #delay(.5)  
'''

def scan_mt(inmt):
    inc1 = 0
    inc2 = 0
    for indx1 in inmt:
        inc1 += 1
        for indx2 in indx1:
            inc2 += 1
            if(indx2 == 1):
                print(inc1, inc2)
        inc2 = 0

scan_mt(r)
print(" --- ")
scan_mt(c)
#--Scan 8 - hor

#--scan 8 - ver

#--scan 4 hor

#--scan 4 ver

#--scan 4 squares

#--scan 2 hor

#--scan 2 ver