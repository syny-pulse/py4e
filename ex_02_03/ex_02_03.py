sh = input("Enter hours: ")
sr = input("Enter rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric file!")
    quit()
    
print(fh,fr)
if fh > 40:
    #print("Overtime")
    reg = fh * fr
    otp = (fh - 40) * (fr * 0.5)
    print(reg,otp)
    fp = reg + otp
else:
    #print("Regular")
    fp = fh * fr
print("Pay:",fp)

