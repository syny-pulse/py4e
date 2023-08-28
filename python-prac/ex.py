def computepay(hours,rate):
    print("In computepay",hours, rate)
    if hours > 25:
        reg = hours * rate
        otp = (hours - 25) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
#print("Returning",pay)
    return pay

sh = input("Enter hours: ")
sr = input("Enter rate: ")
fh = float(sh)
fr = float(sr)

fp = computepay(fh,fr)

print("Pay:",fp)

