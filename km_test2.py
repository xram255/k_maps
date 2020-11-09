import numpy as np

smdict = {'volvo': 89, 'honda': 92, 'Toyota': 98}
#mdict = smdict.copy()
smlist = ['yellow', 25, 89, 'sunshine']

npdict = np.array([[{'abcd': 0}, {'abcD': 0}]])

mdict = {}
names = ['john', 'juan', 'jason', 'jenny']
ages = [32, 45, 25, 37]

if __name__ == "__main__":
    
    for inc in range (len(names)):
        mdict[names[inc]] = ages[inc]

    print(mdict)
    #print(smdict.values()[1])
    '''
    del smdict['Toyota']
    for inc in smdict:
        print(inc)
    
    print(mdict.keys())
    print(smlist[3])
    
    smdict.update({'Tesla': 2018})
    print(smdict)
    '''
    #print(npdict[0][0])