import numpy as np

smdict = {'volvo': 89, 'honda': 92, 'Toyota': 98}
#mdict = smdict.copy()
smlist = ['yellow', 25, 89, 'sunshine']

if __name__ == "__main__":
    
    print(smdict.values()[1])
    '''
    del smdict['Toyota']
    for inc in smdict:
        print(inc)
    
    print(mdict.keys())
    print(smlist[3])
    
    smdict.update({'Tesla': 2018})
    print(smdict)
    '''