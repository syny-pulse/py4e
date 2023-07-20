num = 0.0
tot = 0.0
while True:
    sval = input('Enter number: ')
    if sval == 'done':
        break
    try:
        fval = int(sval)
    except:
        print('Invalid input')
        continue
    #print(fval)
    num = num + 1
    tot = tot + fval
#print('ALL DONE')
print(num,tot,tot/num)
