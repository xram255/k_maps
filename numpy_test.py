import numpy as np

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
    print(strl)
    strr = scan_str2(strc, strd)
    print(strr)
    outstr = scan_str2(strl, strr)
    return outstr

print(scan_str4(r3c1, r3c2, r4c1, r4c2))
#print(scan_str2(r3c1, r3c2))