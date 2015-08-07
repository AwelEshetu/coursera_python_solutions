
#prompt the user for inputs
hrs=raw_input("Enter hours:")
hours=float(hrs)
rts=raw_input("Enter hourly rate:")
rates=float(rts)
#computing logic
def computepay(h,r):
    if h>40:
        payment= (40*r)+((h-40)*r*1.5)
    else:
        payment=h*r
    return payment
p=computepay(hours,rates)
print "Your payment is:" , p
