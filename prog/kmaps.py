import numpy as np

x = 2

rows = np.array([[{'abcd': 0}, {'abcD': 0}, {'abCD': 0}, {'abCd': 0}],
                 [{'aBcd': 0}, {'aBcD': x}, {'aBCD': 2}, {'aBCd': 0}],
                 [{'ABcd': 1}, {'ABcD': 1}, {'ABCD': 1}, {'ABCd': x}],
                 [{'Abcd': 0}, {'AbcD': 1}, {'AbCD': 1}, {'AbCd': 0}]])

cols = rows.T

#--Read from matrix---
def read_key(type, inrow, incol):
    return list(type[inrow][incol].keys())[0]

def read_val(type, inrow, incol):
    return list(type[inrow][incol].values())[0]
#---End of read from matrix---
#=====Scan Strings=========
def scan_str2(stra, strb): # 2 Strings
    outstr =''
    for num in range(len(stra)):
        if stra[num] == strb[num]:
            outstr += stra[num]
    return outstr

def scan_str4(stra, strb, strc, strd): # 4 Strings
    strl = scan_str2(stra, strb)
    #print(strl)
    strr = scan_str2(strc, strd)
    #print(strr)
    outstr = scan_str2(strl, strr)
    return outstr

def  scan_str8(st, a): # 8 Strings
    b = a + 1
    if b > 3:
        b = 0
    stru = scan_str4(st[a][0], st[a][1], st[a][2], st[a][3])
    strd = scan_str4(st[b][0], st[b][1], st[b][2], st[b][3])
    outstr = scan_str2(stru, strd)
    return outstr
#=====End of Scan Strings==========

if __name__=="__main__":
    #print(list(km_inps[3][2].keys())[0])
    #print(read_key(rows, 1, 1), read_val(rows, 1, 1))
    pass