import numpy as np
from time import sleep as delay

r = np.array([[1, 0, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 1, 1]])

r_str = np.array([['abcd', 'abcD', 'abCD', 'abCd'],
                  ['aBcd', 'aBcD', 'aBCD', 'aBCd'],
                  ['ABcd', 'ABcD', 'ABCD', 'ABCd'],
                  ['Abcd', 'AbcD', 'AbCD', 'AbCd']])


c = r.T

#print(r_str[0][3])
#print(r, '\n\n', c)
#--Scan All--

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

'''
scan_mt(r)
print("---")
scan_mt(c)
print('===')
'''
#--Scan 8 - hor
def scan8hor():
    outlist = []
    num_po = 0
    for num in range(4):
        num_po += 1
        if num_po > 3:
            num_po = 0
        if(r[num].all() and r[num_po].all()):
            outlist.append(num)
            #print(num, num_po, 'all true')
    return outlist

#--scan 8 - ver

#--scan 4 hor

#--scan 4 ver

#--scan 4 squares

#--scan 2 hor

#--scan 2 ver


# Returning multiple values
def mult_return():
    gr = "answer is "
    v = 54
    return [gr, v]

#nlist = [[0, 0, 0, 1], [1, 0, 0, 1]]

if __name__ =="__main__":
    print("neon")
    #print(mult_return()[1])
    #print(scan8hor())
    #print(len(scan8hor()))
    #print(r, '\n',nlist)


