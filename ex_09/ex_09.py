fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:
            di[w] = di.get(w,0) + 1
            #print(w,'new',di[w])           
        
    #print(di)
    largest = -1
    theword = None
    for k,v in di.items() :
          if v>largest:
                largest = v
                theword = k
print(theword,largest)
