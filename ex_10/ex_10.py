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
        
    print(di)
tmp = list()
for k,v in di.items() :
      #print(k,v)
      newt = (v,k)
      tmp.append(newt)
print ('Flipped', tmp)
tmp = sorted(tmp, reverse=True)
print('Sorted',tmp)

for v,k in tmp[:5]:
      print(k,v)
