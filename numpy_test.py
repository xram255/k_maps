import numpy as np
import km_test1 as kmt

'''
a = np.matrix('1, 2; 3, 4; 5, 6')
b = np.array([[2, 3],
             [4, 5],
             [6, 7]])

c = np.matrix([[7, 8],
               [9, 11],
               [1, 2]])

#print(a, "\n", a.T)

km = np.array([[0, 0, 0, 0],
               [0, 0, 0, 0],
               [1, 1, 1, 0], 
               [0, 1, 0, 0]])

#print(km.__eq__(1))
'''
'''
if 'hello' in 'hello world':
    print('we found it')
'''
r3c1 = 'ABcd'
r3c2 = 'ABcD'
r4c1 = 'Abcd'
r4c2 = 'AbcD'


def scan_str2(stra, strb):
    outstr =''
    for num in range(len(stra)):
        if stra[num] == strb[num]:
            outstr += stra[num]
    return outstr


def scan_str4(stra, strb, strc, strd):
    strl = scan_str2(stra, strb)
    #print(strl)
    strr = scan_str2(strc, strd)
    #print(strr)
    outstr = scan_str2(strl, strr)
    return outstr

def  scan_str8(st, a):
    b = a + 1
    if b > 3:
        b = 0
    stru = scan_str4(st[a][0], st[a][1], st[a][2], st[a][3])
    strd = scan_str4(st[b][0], st[b][1], st[b][2], st[b][3])
    outstr = scan_str2(stru, strd)
    return outstr

#print(scan_str4(r3c1, r3c2, r4c1, r4c2))
#print(scan_str2(r3c1, r3c2))

'''
arr1 = np.array([[1, 0, 1, 1],
                 [1, 1, 1, 1]])


if(arr1[0].all() == True):
    print("all values are true ")
else:
    print("all values are not true")
'''

#print(kmt.scan8hor())
print(len(kmt.scan8hor()))

print(scan_str8(kmt.r_str, kmt.scan8hor()[0]))

#print(kmt.r_str[0])


