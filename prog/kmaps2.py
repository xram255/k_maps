import numpy as np

#-- Constant values--
X = 32 # 2^6, 

#                   C0      C1      C2      C3
ROW = np.array([['abcd', 'abcD', 'abCD', 'abCd'],  # R1
                ['aBcd', 'aBcD', 'aBCD', 'aBCd'],  # R2
                ['ABcd', 'ABcD', 'ABCD', 'ABCd'],  # R3
                ['Abcd', 'AbcD', 'AbCD', 'AbCd']]) # R4

COL = ROW.T
#-------------------------
# -- Inputs----
row = np.array([[0, 0, 0, 0],
                [1, X, 0, 0],
                [1, 1, 1, X],
                [1, 0, 1, 0]])

col = row.T
#-----------------------------
outv = 0
for inc1 in row:
    for inc2 in inc1:
        outv = outv + inc2
    print(outv & 0b011111)

# --- Read from Matrix ---
def read2(indata, start1, start2): # indata = ROW or COL, start1 = row, start2 = col
    start2_plus1 = start2 + 1
    if start2_plus1 >= 3:
        start2_plus1 = 0
    return [indata[start1][start2], indata[start1][start2_plus1]]

def read4sqr(indata, start1, start2):# indata = ROW or COL, start1 = row, start2 = col
    outstring1 = read2(indata, start1, start2)
    outstring2 = read2(indata, start1 + 1, start2)
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



if __name__=="__main__":
    pass
    
    