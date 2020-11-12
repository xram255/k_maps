import numpy as np

#-- Constant values--
X = 2

#                   C0      C1      C2      C3
ROW = np.array([['abcd', 'abcD', 'abCD', 'abCd'],  # R1
                ['aBcd', 'aBcD', 'aBCD', 'aBCd'],  # R2
                ['ABcd', 'ABcD', 'ABCD', 'ABCd'],  # R3
                ['Abcd', 'AbcD', 'AbCD', 'AbCd']]) # R4

COL = ROW.T
#-------------------------
# -- Inputs----
row = np.array([[0, 0, 0, 0],
                [0, X, 0, 0],
                [1, 1, 1, X],
                [0, 0, 1, 0]])

col = row.T
#-----------------------------
# --- Read from Matrix ---
def read8(indata, starting): # indata=Row or Column, Starting=Starting cell Row OR Column number
    start_plus_one = 0
    if starting >= 3: # row(or column) length = 4
        start_plus_one = 0
    else:
        start_plus_one = starting + 1 # Neibouring row(column)
    return (list(indata[starting]) + list(indata[start_plus_one]))
# ------------------------

#=====Scan Strings=========
#strns = ['abcd', 'abcD', 'abCD', 'abCd', 'aBcd','aBcD', 'aBCD', 'aBCd']

def scan2str(inlist): # Scan list of two strings, two strings has to be the same lenght
    outstr = ''
    for inc in range (len(inlist[0])): # increment for num of letters in first string in list
        if (inlist[0][inc] == inlist[1][inc]): # compare each letter 
            outstr += inlist[0][inc] # added to outstring if matched 
    return outstr

def scan4str(inlist): # Scan list of 4 strings 
    inlist1 = [inlist[0], inlist[1]] # creates list 1
    inlist2 = [inlist[2], inlist[3]]
    strl = scan2str(inlist1) # compare
    strr = scan2str(inlist2)
    return scan2str([strl, strr])

def scan8str(inlist): # Scan list of 8 strings
    inlist1 = [inlist[0], inlist[1], inlist[2], inlist[3]]
    inlist2 = [inlist[4], inlist[5], inlist[6], inlist[7]]
    str1 = scan4str(inlist1)
    str2 = scan4str(inlist2)
    return scan2str([str1, str2])


#=====End of Scan Strings==========       



if __name__=="__main__":
    pass
    
    