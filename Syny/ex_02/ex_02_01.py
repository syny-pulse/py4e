x = input('Enter score: ')
if isinstance(x, str) or x > 1.0:
    print('Bad score')
elif(x >= 0.9):
    print('A')
elif(x >= 0.8):
    print('B')
elif(x >= 0.7):
    print('C')
elif(x >= 0.6):
    print('D')
else:
    print('F')

