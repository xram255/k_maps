import numpy as np

#-- Constant values--
X = 2 # 2^6, 

#                   C0      C1      C2      C3
ROW = np.array([['abcd', 'abcD', 'abCD', 'abCd'],  # R1
                ['aBcd', 'aBcD', 'aBCD', 'aBCd'],  # R2
                ['ABcd', 'ABcD', 'ABCD', 'ABCd'],  # R3
                ['Abcd', 'AbcD', 'AbCD', 'AbCd']]) # R4

COL = ROW.T
#-------------------------
# -- Inputs----
'''
row = np.array([[0, 0, 0, 0],
                [0, 0, X, 0],
                [1, 1, 1, X],
                [0, 1, 0, 0]])
'''
row = np.array([[1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1]])

col = row.T
#-----------------------------

def row2list(): # All data in 16 cells output as a list
    outlist = []
    for inc1 in row:
        for inc2 in inc1:
            outlist.append(inc2)
    return outlist

#print(row2list().count(1) + row2list().count(2))
#print(nums2group(list_out()))

# --- Read from Matrix ---
def read2(indata, start1, start2): # indata = ROW or COL, start1 = row, start2 = col
    start2_plus1 = start2 + 1
    if start2_plus1 >= 3:
        start2_plus1 = 0
    return [indata[start1][start2], indata[start1][start2_plus1]]

def read4sqr(indata, start1, start2):# indata = ROW or COL, start1 = row, start2 = col
    start1_plus1 = start1 + 1
    if start1_plus1 >= 3:
        start1_plus1 = 0
    outstring1 = read2(indata, start1, start2)
    outstring2 = read2(indata, start1_plus1, start2)
    return outstring1 + outstring2

def read8(indata, start): # indata=Row or Column, Starting=Starting cell Row OR Column number
    start_plus1 = start + 1
    if start_plus1 >= 3: # row(or column) length = 4
        start_plus1 = 0
    return (list(indata[start]) + list(indata[start_plus1]))
# -------------End of read from matrix -----------

#=====compare Strings=========
#strns = ['abcd', 'abcD', 'abCD', 'abCd', 'aBcd','aBcD', 'aBCD', 'aBCd']

def comp2str(inlist): # compare list of two strings, two strings has to be the same lenght
    outstr = ''
    for inc in range (len(inlist[0])): # increment for num of letters in first string in list
        if (inlist[0][inc] == inlist[1][inc]): # compare each letter 
            outstr += inlist[0][inc] # added to outstring if matched 
    return outstr

def comp4str(inlist): # compare list of 4 strings 
    inlist1 = [inlist[0], inlist[1]] # creates list 1
    inlist2 = [inlist[2], inlist[3]]
    strl = comp2str(inlist1) # compare
    strr = comp2str(inlist2)
    return comp2str([strl, strr])

def comp8str(inlist): # compare list of 8 strings
    inlist1 = [inlist[0], inlist[1], inlist[2], inlist[3]]
    inlist2 = [inlist[4], inlist[5], inlist[6], inlist[7]]
    str1 = comp4str(inlist1)
    str2 = comp4str(inlist2)
    return comp2str([str1, str2]) # returns similar characters only


#=====End of comp Strings==========       

# ----------Scan ------------------

def scan_all():
    if row.all() == 1:
        print('all 1')

def scan8(indata, start): #indata = row, col | # start = 0, 1, 2, 3
    start_plus1 = start + 1
    if start_plus1 >= 3:
        start_plus1 = 0
    if indata[start].all() > 0 and indata[start_plus1].all() > 0:
        print(' 8 ones')

#print(read4sqr(row, 0, 0))

def scan4(indata): # use read4sqr()  or list(row(n)) or list(col(n)) to input da
    if indata.count(1) == 4:
        print('4 ones found')

def scan2(indata): # use read2(row, n, m) to input data
    if indata.count(1) == 2:
        print('2 ones found')

#scan2(read2(row, 0, 0))    
#scan4(read4sqr(row, 3, 3))
#scan4(list(row[0]))

if __name__=="__main__":
    pass
    
    