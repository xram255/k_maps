import numpy as np

x = 2
'''
rows = np.array([[{'abcd': 0}, {'abcD': 0}, {'abCD': 0}, {'abCd': 0}],
                 [{'aBcd': 0}, {'aBcD': x}, {'aBCD': 2}, {'aBCd': 0}],
                 [{'ABcd': 1}, {'ABcD': 1}, {'ABCD': 1}, {'ABCd': x}],
                 [{'Abcd': 0}, {'AbcD': 1}, {'AbCD': 1}, {'AbCd': 0}]])
'''

ROW = np.array([['abcd', 'abcD', 'abCD', 'abCd'],
                ['aBcd', 'aBcD', 'aBCD', 'aBCd'],
                ['ABcd', 'ABcD', 'ABCD', 'ABCd'],
                ['Abcd', 'AbcD', 'AbCD', 'AbCd']])

row = np.array([[0, 0, 0, 0],
                [0, x, 0, 0],
                [1, 1, 1, x],
                [0, 0, 1, 0]])

col = row.T

print(ROW)

#--Read from matrix---
def read_key(type, inrow, incol): #type = rows or cols
    return list(type[inrow][incol].keys())[0]

def read_val(type, inrow, incol):
    return list(type[inrow][incol].values())[0]

def read4key(type, linev): #  type = rows or cols, linev = row or col num
    return list(type[linev]) # returns 4 horizontal or vertical values


#---End of read from matrix---

#=====Scan Strings=========
#strns = ['abcd', 'abcD', 'abCD', 'abCd', 'aBcd','aBcD', 'aBCD', 'aBCd']

def scan2(inlist):
    outstr = ''
    for inc in range (len(inlist[0])): # increment for num of letters in first string in list
        if (inlist[0][inc] == inlist[1][inc]): # compare each letter 
            outstr += inlist[0][inc] # added to outstring if matched 
    return outstr

def scan4(inlist):
    inlist1 = [inlist[0], inlist[1]] # creates list 1
    inlist2 = [inlist[2], inlist[3]]
    strl = scan2(inlist1) # compare
    strr = scan2(inlist2)
    return scan2([strl, strr])

def scan8(inlist):
    inlist1 = [inlist[0], inlist[1], inlist[2], inlist[3]]
    inlist2 = [inlist[4], inlist[5], inlist[6], inlist[7]]
    str1 = scan4(inlist1)
    str2 = scan4(inlist2)
    return scan2([str1, str2])


#=====End of Scan Strings==========       



if __name__=="__main__":
    #print(list(km_inps[3][2].keys())[0])
    #print(read_key(rows, 1, 1), read_val(rows, 1, 1))
    pass
    