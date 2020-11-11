import numpy as np

smdict = {'volvo': 89, 'honda': 92, 'Toyota': 98}
#mdict = smdict.copy()
smlist = ['yellow', 25, 89, 'sunshine']

npdict = np.array([[{'abcd': 0}, {'abcD': 0}]])

mdict = {}
names = ['john', 'juan', 'jason', 'jenny']
ages = [32, 45, 25, 37]

dict0 = {1 : 'Neo', 2: 'Trinity'}
empty_list = []
dict1 = dict(jamal = 24, harris = 32, samantha = 17, tom = 25)
tuple1 = 'jenny', 23
tuple2 = 'juanito', 44
dict2 = dict([tuple1, tuple2])
if __name__ == "__main__":
    print(dict2.items())
    #print(list(dict0.values())[0])
    #print(max(1, 4, 5))
    #print(min(dict0.keys()))
    '''
    for inc in range (len(names)):
        mdict[names[inc]] = ages[inc]
    '''
    #print(mdict)
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